#!/usr/bin/env python3
"""Rank model × instruction configurations from reviewed experiment CSV records.

This tool is deliberately fail-closed: only configurations with complete six-axis
records, repeated independent runs, evidence, reviewer approval, no critical
failures, and passing score floors are ranked. It uses only the Python standard
library.
"""
import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

AXES = ("ethics", "speed", "capability", "accuracy", "cost", "depth")
FLOORS = {"ethics": 5, "speed": 3, "capability": 3, "accuracy": 3, "cost": 3, "depth": 3}
TRUE = {"yes", "true", "1", "approved"}
FALSE = {"", "no", "false", "0", "none"}
REQUIRED = {
    "experiment_id", "task_id", "model_id", "model_version",
    "instruction_id", "instruction_version", "agent_config_id", "run_id",
    "axis", "score", "latency_ms", "total_cost", "currency",
    "critical_failure", "evidence_ref", "reviewer", "review_status", "decision",
}

def number(value):
    if value is None or str(value).strip() == "":
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if result >= 0 else None

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", nargs="?", default="tests/experiment-results.csv")
    parser.add_argument("--objective", choices=("balanced", "quality", "latency", "cost"), default="balanced")
    parser.add_argument("--min-runs", type=int, default=3)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args(argv)
    if args.min_runs < 1:
        parser.error("--min-runs must be >= 1")

    path = Path(args.csv_path)
    if not path.is_file():
        print(f"REJECT: results file not found: {path}", file=sys.stderr)
        return 2
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            print("REJECT: missing columns: " + ", ".join(sorted(missing)), file=sys.stderr)
            return 2
        rows = list(reader)

    groups = defaultdict(list)
    errors = []
    for line, row in enumerate(rows, start=2):
        axis = (row.get("axis") or "").strip().lower()
        if axis not in AXES:
            errors.append(f"line {line}: unknown axis {axis!r}")
            continue
        key_fields = ("experiment_id", "task_id", "model_id", "model_version",
                      "instruction_id", "instruction_version", "agent_config_id", "run_id")
        if any(not (row.get(k) or "").strip() for k in key_fields):
            errors.append(f"line {line}: missing configuration/run identity")
            continue
        key = tuple((row.get(k) or "").strip() for k in key_fields[:-1])
        run_id = (row.get("run_id") or "").strip()
        if run_id.startswith("self-eval-"):
            errors.append(f"line {line}: self-evaluation run is not eligible evidence")
        try:
            score = int(row.get("score", ""))
            if score < 1 or score > 5:
                raise ValueError
        except ValueError:
            errors.append(f"line {line}: score must be an integer from 1 to 5")
            continue
        status = (row.get("review_status") or "").strip().lower()
        if status not in TRUE:
            errors.append(f"line {line}: review_status must be approved")
        if not (row.get("reviewer") or "").strip() or not (row.get("evidence_ref") or "").strip():
            errors.append(f"line {line}: reviewer and evidence_ref are required")
        critical = (row.get("critical_failure") or "").strip().lower()
        if critical not in FALSE:
            errors.append(f"line {line}: critical failure; configuration is ineligible")
        if (row.get("decision") or "").strip().lower() not in {"pass", "accepted", "accept"}:
            errors.append(f"line {line}: decision must be PASS/ACCEPTED")
        groups[key].append((row, axis, score))

    candidates = []
    for key, entries in groups.items():
        identity = dict(zip(("experiment_id", "task_id", "model_id", "model_version",
                             "instruction_id", "instruction_version", "agent_config_id"), key))
        by_run = defaultdict(dict)
        run_bad = False
        for row, axis, score in entries:
            run_id = (row.get("run_id") or "").strip()
            if axis in by_run[run_id]:
                errors.append(f"{identity['agent_config_id']}/{run_id}: duplicate axis {axis}")
                run_bad = True
            by_run[run_id][axis] = (row, score)
        if len(by_run) < args.min_runs:
            errors.append(f"{identity['agent_config_id']}: {len(by_run)} runs; need {args.min_runs}")
            run_bad = True
        for run_id, axis_map in by_run.items():
            absent = set(AXES) - set(axis_map)
            if absent:
                errors.append(f"{identity['agent_config_id']}/{run_id}: missing axes {', '.join(sorted(absent))}")
                run_bad = True
            for axis, (_, score) in axis_map.items():
                if score < FLOORS[axis]:
                    errors.append(f"{identity['agent_config_id']}/{run_id}: {axis} score {score} below floor {FLOORS[axis]}")
                    run_bad = True
        if run_bad:
            continue

        scores = {axis: [axis_map[axis][1] for axis_map in by_run.values()] for axis in AXES}
        latencies, costs, currencies = [], [], set()
        for axis_map in by_run.values():
            # Timing/cost can be repeated across the six axis rows; count once per run.
            representative = next(iter(axis_map.values()))[0]
            latency = number(representative.get("latency_ms"))
            cost = number(representative.get("total_cost"))
            if latency is not None:
                latencies.append(latency)
            if cost is not None:
                costs.append(cost)
                currencies.add((representative.get("currency") or "").strip())
        if args.objective in {"latency", "cost"} and (not latencies if args.objective == "latency" else (not costs or len(currencies) != 1)):
            errors.append(f"{identity['agent_config_id']}: missing comparable {args.objective} measurements")
            continue
        mean_scores = {axis: round(statistics.mean(values), 3) for axis, values in scores.items()}
        quality = statistics.mean(mean_scores[a] for a in ("capability", "accuracy", "depth"))
        if args.objective == "quality":
            objective_score = quality
        elif args.objective == "latency":
            objective_score = -statistics.mean(latencies)
        elif args.objective == "cost":
            objective_score = -statistics.mean(costs)
        else:
            objective_score = statistics.mean(mean_scores[a] for a in ("speed", "capability", "accuracy", "cost", "depth"))
        candidates.append({**identity, "runs": len(by_run), "scores": mean_scores,
                           "quality_mean": round(quality, 3),
                           "mean_latency_ms": round(statistics.mean(latencies), 3) if latencies else None,
                           "mean_cost": round(statistics.mean(costs), 6) if costs else None,
                           "currency": next(iter(currencies)) if len(currencies) == 1 else None,
                           "objective": args.objective, "objective_score": round(objective_score, 6)})

    candidates.sort(key=lambda item: item["objective_score"], reverse=True)
    if args.json:
        print(json.dumps({"eligible": candidates, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        if not candidates:
            print("NO ELIGIBLE CONFIGURATIONS")
        else:
            print(f"Eligible configurations (objective={args.objective}):")
            for i, item in enumerate(candidates, start=1):
                print(f"{i}. {item['model_id']}@{item['model_version']} × "
                      f"{item['instruction_id']}@{item['instruction_version']} "
                      f"[{item['agent_config_id']}] runs={item['runs']} "
                      f"quality={item['quality_mean']} objective={item['objective_score']} "
                      f"latency_ms={item['mean_latency_ms']} cost={item['mean_cost']} {item['currency'] or ''}")
        if errors:
            print(f"\nExcluded/invalid records: {len(errors)}")
            for error in errors:
                print(f"- {error}")
    # An empty eligible set is not a successful optimization result.
    return 0 if candidates and not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())

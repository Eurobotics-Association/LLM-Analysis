#!/usr/bin/env python3
"""Summarize DeepSWE v1.1 trial evidence; does not calculate or publish prices."""
import argparse
import collections
import json

FIELDS = ("n_input_tokens", "n_uncached_input_tokens", "n_cache_read_tokens",
          "n_cache_write_tokens", "n_output_tokens", "peak_context_tokens")


def summarize(data):
    rows = data["rows"]
    scored = [r for r in rows if r.get("source") == "deep-swe"
              and r.get("eval_scope") == "full" and r.get("included_in_score") is True]
    groups = collections.defaultdict(list)
    for row in scored:
        groups[(row["model"], row.get("reasoning_effort"))].append(row)
    results = []
    for (model, effort), trials in sorted(groups.items(), key=lambda item: str(item[0])):
        results.append({
            "model": model, "effort": effort, "scored_trials": len(trials),
            "tasks": len({r["task_name"] for r in trials}),
            "providers": dict(sorted(collections.Counter(str(r.get("provider")) for r in trials).items())),
            "fields_present": {f: sum(r.get(f) is not None for r in trials) for f in FIELDS},
        })
    return {"all_trials": len(rows), "scored_official_full_trials": len(scored), "groups": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trial_index", help="Path to a downloaded, frozen official trials.json")
    parser.add_argument("--model", action="append", help="Exact model ID; repeat to select multiple")
    args = parser.parse_args()
    with open(args.trial_index, encoding="utf-8") as stream:
        result = summarize(json.load(stream))
    if args.model:
        result["groups"] = [row for row in result["groups"] if row["model"] in args.model]
        result["models_not_found"] = sorted(set(args.model) - {row["model"] for row in result["groups"]})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

import argparse
import json


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--results", required=True)
    args = p.parse_args()
    print(json.dumps(json.loads(open(args.results, "r", encoding="utf-8").read()), indent=2))


if __name__ == "__main__":
    main()

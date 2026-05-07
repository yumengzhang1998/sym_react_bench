import argparse

from topokin.config import load_config
from topokin.io.synthetic_generator import generate_dataset


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    args = p.parse_args()
    cfg = load_config(args.config)
    out = generate_dataset(cfg.get("dataset_dir", "data/synthetic/demo"), cfg.get("element", "Bi"), cfg.get("frames", 60), cfg.get("seed", 0))
    print(out)


if __name__ == "__main__":
    main()

"""Small helper to download datasets used in notebooks or case files."""

import os
from pathlib import Path


def ensure_data_dir(path: str = "datasets") -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def download_sample_csv(path: str = "datasets/sample.csv"):
    p = ensure_data_dir()
    # Placeholder: replace with real download logic if needed
    if not p.joinpath("sample.csv").exists():
        with open(p.joinpath("sample.csv"), "w", encoding="utf-8") as f:
            f.write("x,y\n1,2\n3,4\n")
    return p.joinpath("sample.csv")


if __name__ == "__main__":
    print("Created sample dataset:", download_sample_csv())

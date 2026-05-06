from pathlib import Path
import textwrap

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASETS_DIR = PROJECT_ROOT / "datasets"

INSTRUCTIONS = """
Datasets are not redistributed from an author-owned archive during double-blind review.

Please download the datasets from their original public sources and place them under:

    {datasets_dir}

Expected structure:

    datasets/
        insects/
        synthetic/
        ...

A permanent archival mirror will be added after the review period.
""".format(datasets_dir=DATASETS_DIR)


def main():
    if DATASETS_DIR.exists():
        print("Datasets already present.")
        return

    raise RuntimeError(textwrap.dedent(INSTRUCTIONS).strip())


if __name__ == "__main__":
    main()

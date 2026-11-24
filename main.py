#!/usr/bin/env python3
"""Write this competition's single roast line to /output/entry.txt."""

from pathlib import Path

ROAST = "My agent said the deployment was safe. It said so from inside the rollback."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise ValueError("ROAST must be 1 to 200 non-blank characters")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()

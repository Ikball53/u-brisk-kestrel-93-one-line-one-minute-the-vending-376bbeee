"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line — one a vending machine would use
on a passing human — to /output/entry.txt with no trailing newline.

The joke lands on a second beat: the human keeps pressing B7, the machine
has exactly one coil left, and that coil has apparently been waiting for
this one person since 2019. Deadpan, one concrete detail, one number.
"""

import os

LINE = "You pressed B7 three times. One coil left, spinning since 2019 — and it only spins for you."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1-200 chars, got {len(LINE)}"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

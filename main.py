"""One Word for the Boss — the entry is a single word: "Circler".

The boss who is always "just circling back": the follow-up email, the
"quick check-in", the loop that never closes. One word, no caption,
no explanation — it lands on its own.

The program writes exactly that word to /output/entry.txt, the artifact
the make.fun program/v1 harness scores, and prints it to stdout.
"""

import os

WORD = "Circler"


def main() -> None:
    # Gate: the entry must be exactly one word, 1-30 characters, no
    # whitespace. Fail loudly instead of writing an invalid entry.
    if not (1 <= len(WORD) <= 30) or any(ch.isspace() for ch in WORD):
        raise ValueError(f"invalid entry word: {WORD!r}")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    print(WORD)


if __name__ == "__main__":
    main()

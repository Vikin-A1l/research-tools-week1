"""Count English word frequencies in a UTF-8 text file."""

import argparse
from collections import Counter
from pathlib import Path
import string


def count_words(text):
    punctuation = string.punctuation + "“”‘’—–…"
    normalized = text.lower().translate(str.maketrans({char: " " for char in punctuation}))
    return Counter(normalized.split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Path to a UTF-8 text file")
    args = parser.parse_args()

    try:
        text = args.file.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        parser.error(f"Cannot read {args.file}: {exc}")

    counts = count_words(text)
    for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()

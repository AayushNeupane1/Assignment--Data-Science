"""File handling - text files: write, append, read, with error handling.
Reworked from FileHandling 1.py/2.py/3.py. Run: python text_files.py
"""

import os

PATH = "data/notes.txt"


def main():
    os.makedirs("data", exist_ok=True)

    # write (overwrites)
    with open(PATH, "w") as f:
        f.write("first line\n")
        f.write("second line\n")

    # append
    with open(PATH, "a") as f:
        f.write("third line\n")

    # read whole file + count words/lines
    try:
        with open(PATH, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("file not found")
        return

    print("contents:\n" + content, end="")
    print("words:", len(content.split()))
    print("lines:", len(content.splitlines()))


if __name__ == "__main__":
    main()

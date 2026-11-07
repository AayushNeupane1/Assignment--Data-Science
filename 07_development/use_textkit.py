"""Development - using the local 'textkit' package. Run: python use_textkit.py"""

from textkit import word_count, char_count, top_word
import textkit


def main():
    text = "the quick brown fox the lazy dog the end"
    print("textkit version:", textkit.__version__)
    print("words      :", word_count(text))
    print("chars       :", char_count(text))
    print("chars+spaces:", char_count(text, include_spaces=True))
    print("top word    :", top_word(text))


if __name__ == "__main__":
    main()

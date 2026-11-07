"""Advanced - regular expressions with the re module.
Reworked from the lab exercise. Run: python regex_demo.py
"""

import re


def main():
    text = "Contact Ram at ram@example.com or call 0401-234-567 in London."

    # findall returns every match of a pattern
    capitalised = re.findall(r"[A-Z][a-z]+", text)
    print("capitalised words:", capitalised)      # ['Contact', 'Ram', 'London']

    emails = re.findall(r"[\w.]+@[\w.]+", text)
    print("emails           :", emails)            # ['ram@example.com']

    digits = re.findall(r"\d+", text)
    print("digit groups     :", digits)            # ['0401', '234', '567']

    # search finds the first match (or None); .group() gets the text
    match = re.search(r"\d{4}-\d{3}-\d{3}", text)
    print("phone            :", match.group() if match else "none")


if __name__ == "__main__":
    main()

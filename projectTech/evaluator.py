import nltk
from nltk.corpus import words, names
import string
import re

nltk.download("words")
nltk.download("names")


def is_valid_password(password):
    criteries = {
        "length": len(password) >= 8,
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special_char": any(c in string.punctuation for c in password),
        "common_words": False,
        "common_names": False,
    }

    common_words = set(words.words())
    common_names = set(n.lower() for n in names.words())

    for part in re.findall(r"[a-zA-Z]+", password):
        if part.lower() in common_words:
            criteries["common_words"] = True
        if part.lower() in common_names:
            criteries["common_names"] = True

    score = sum(v for v in criteries.values() if v is True)

    if score >= 6:
        level = "Very Strong"
    elif score >= 4:
        level = "Strong"
    else:
        level = "Weak"

    return criteries, level

import nltk
from nltk.corpus import words, names
import string
import re

nltk.download("words")
nltk.download("names")


# This function evaluates the strength of a password based on various criteria.
# It checks for length, presence of lowercase and uppercase letters, digits,
# special characters, and the presence of common words or names.
# The password is scored based on these criteria, and categorized into levels:
# "Very Strong", "Strong", or "Weak".
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

    # The words.words() provides a list of common English words,
    # and names.words() provides a list of common names.
    # These lists are used to check if the password contains common words or names,
    # which can weaken the password's strength.
    # Downloading these resources ensures that the function has access to them.

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

import random
from dictionaries import adjetives, nouns, verbs, simbols


def token_for_word(token):
    letters = "".join([c for c in token if c.isalpha()])
    digits = "".join([c for c in token if c.isdigit()])
    symbols = "".join([c for c in token if not c.isalnum()])

    word1 = random.choice(adjetives)
    word2 = random.choice(nouns)
    word3 = random.choice(verbs)
    end_symbol = symbols if symbols else random.choice(simbols)
    number = digits if digits else str(random.randint(10, 99))

    return f"{word1}{word2}{number}{word3}{end_symbol}"


def generate_nmenotecnic_version(tokens):
    return token_for_word(random.choice(tokens))

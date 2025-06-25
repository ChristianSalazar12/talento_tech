import random
from dictionaries import adjetives, nouns, verbs, simbols

# This function takes a token (a string) and generates a mnemonic version of it.
# It extracts letters, digits, and symbols from the token,
# and then randomly selects words from predefined lists of adjectives, nouns, and verbs.
# The generated mnemonic consists of a random adjective, noun, number, verb, and an optional
# symbol from the token or a random symbol from a predefined list.
# The function returns the mnemonic as a string.
# This can be useful for creating memorable passwords or identifiers.
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

## This function generates a mnemonic version of a list of tokens.
# It takes a list of tokens (strings) and applies the `token_for_word` function
# to each token in the list. The result is a list of mnemonic strings,
# each corresponding to a token from the input list.
def generate_nmenotecnic_version(tokens):
    return token_for_word(random.choice(tokens))

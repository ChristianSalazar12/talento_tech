import random
import string
# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download("punkt")


# This function takes a password as input and returns a list of characters (tokens) from the
# password. Each character in the password is treated as a separate token.
def tokenize_password(password):
    return list(password)

# This function takes a text input and returns a list of characters (tokens) from the text.
# Each character in the text is treated as a separate token.
# It can be used to tokenize any string, such as a sentence or a paragraph.
# This is useful for further processing, such as combining tokens with those from a password.
# The function uses a simple list comprehension to convert the text into a list of characters.
# It can be used in various applications, such as text analysis, natural language processing,
# or generating combinations of characters from different sources.
def tokenize_text(text):
    return list(text)

## This function combines tokens from a base list (tokens_base) with tokens from an extra list (tokens_extra).
# It creates combinations by randomly selecting an extra token and a mode of combination.
# The mode determines how the tokens are combined:
# 1. The extra token is appended to the base token.
# 2. The base token is appended to the extra token.
# 3. A random extra token is appended to the combination of the base and extra tokens
# The function returns a list of combined tokens.
# This can be useful for generating unique identifiers, passwords, or other forms of text
# that require a mix of characters from different sources.
def combinar_por_letra(tokens_base, tokens_extra):
    combinaciones = []
    for letra in tokens_base:
        extra = random.choice(tokens_extra)
        modo = random.choice([1, 2, 3])

        if modo == 1:
            combinado = f"{letra}{extra}"
        elif modo == 2:
            combinado = f"{extra}{letra}"
        else:

            combinado = f"{letra}{extra}{random.choice(tokens_extra)}"

        combinaciones.append(combinado)
    return combinaciones

## This function generates compound tokens by combining tokens from a password and a text.
# It first tokenizes the password and the text into lists of characters.
# Then, it combines these tokens using the `combinar_por_letra` function.
# The resulting list of combined tokens can be used for various purposes, such as creating
# unique identifiers, passwords, or other forms of text that require a mix of characters from
# different sources.
def generar_tokens_compuestos(password, text):
    tokens_base = tokenize_password(password)
    tokens_extra = tokenize_text(text)
    return combinar_por_letra(tokens_base, tokens_extra)

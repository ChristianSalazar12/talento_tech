import random
import string
# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download("punkt")


def tokenize_password(password):
    return list(password)


def tokenize_text(text):
    return list(text)


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


def generar_tokens_compuestos(password, text):
    tokens_base = tokenize_password(password)
    tokens_extra = tokenize_text(text)
    return combinar_por_letra(tokens_base, tokens_extra)

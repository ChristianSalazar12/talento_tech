# stroke.py
import string
import time
from itertools import product


# ---------- Cifrado César (descifrado) ----------
def decrypt_cesar(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


def force_stroke_cessar(ciphertext, target=None):
    """
    Fuerza bruta para descifrar texto cifrado con César.
    Retorna una lista de resultados (shift, texto) y la clave si se encuentra.
    """
    resultados = []
    clave_encontrada = None
    inicio = time.time()

    for d in range(1, 26):
        intento = decrypt_cesar(ciphertext, d)
        resultados.append((d, intento))
        if target and intento.lower() == target.lower():
            clave_encontrada = intento
            break

    fin = time.time()
    return {
        "resultados": resultados,
        "clave_encontrada": clave_encontrada,
        "tiempo": round(fin - inicio, 2),
    }


print(decrypt_cesar("fkulvwldq", 3))


# ---------- Cifrado Vigenère (descifrado) ----------
def decrypt_vigenere(ciphertext, key):
    resultado = ""
    key = (key * (len(ciphertext) // len(key) + 1))[: len(ciphertext)]

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            key_char = key[i].lower()
            shift = ord(key_char) - ord("a")
            resultado += chr((ord(char) - base - shift) % 26 + base)
        else:
            resultado += char
    return resultado


def force_stroke_vigenere(ciphertext, max_length=2, target=None):
    """
    Fuerza bruta para descifrar Vigenère probando todas las combinaciones hasta longitud 'max_length'.
    """
    resultados = []
    clave_encontrada = None
    inicio = time.time()

    alphabet = string.ascii_lowercase
    posibles_claves = [
        "".join(p)
        for l in range(1, max_length + 1)
        for p in product(alphabet, repeat=l)
    ]

    for key in posibles_claves:
        intento = decrypt_vigenere(ciphertext, key)
        resultados.append((key, intento))
        if target and intento.lower() == target.lower():
            clave_encontrada = intento
            break

    fin = time.time()
    return {
        "resultados": resultados,
        "clave_encontrada": clave_encontrada,
        "tiempo": round(fin - inicio, 2),
    }

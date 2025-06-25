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

# add the documentation for decrypt_vigenere function in english
# This function decrypts a given ciphertext using the Vigenère cipher technique.
# It shifts each letter back by the corresponding letter in the key.
# Non-alphabetic characters remain unchanged.
# The function returns the decrypted text as a string.  
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

# # This function performs a brute-force attack on the Vigenère cipher by trying all combinations
# of keys up to a specified maximum length. It returns a list of results with the 
# decrypted text for each key, and the found key if it matches the target.
# The function uses the itertools.product to generate all possible combinations of letters
# from the alphabet for the specified maximum length. It decrypts the ciphertext with each key
# and checks if the decrypted text matches the target. If a match is found, it breaks
# the loop and returns the results along with the found key and the time taken for the operation
# The function is useful for brute-force attacks on Vigenère ciphers, allowing to find
# the key used for encryption by testing all possible combinations of letters.
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

##decrypt_cesar(ciphertext, shift) documentation :
# This function decrypts a given ciphertext using the Caesar cipher technique.
# It shifts each letter back by a specified number of positions (shift).
# Non-alphabetic characters remain unchanged.
# The function returns the decrypted text as a string.
# The shift value should be between 1 and 25, as a shift of 0 would not change the text,
# and a shift of 26 would return the original text.
# The function handles both uppercase and lowercase letters, preserving their case.
# For example, if the ciphertext is "fkulvwldq" and the shift is 3,
# the function will return "césar".
# The function uses the ASCII values of characters to perform the decryption,
# ensuring that the letters wrap around correctly within the alphabet.
# It calculates the base ASCII value for uppercase ('A') or lowercase ('a') letters,
# and applies the shift accordingly using modular arithmetic.
# Non-alphabetic characters (like spaces, punctuation, etc.) are added to the result
# without any changes, ensuring that the structure of the original text is preserved.
# The function is useful for decrypting messages that have been encoded using the Caesar cipher,
# which is a simple substitution cipher where each letter is replaced by another letter
# a fixed number of positions down the alphabet.
# It can be used in various applications, such as cryptography exercises, puzzles, or educational
# purposes to demonstrate basic encryption and decryption techniques.
# It is important to note that the Caesar cipher is not secure for modern applications,
# as it can be easily broken with frequency analysis or brute-force attacks.
# However, it serves as a good introduction to the concepts of encryption and decryption.
# The function can be called with a ciphertext and a shift value to obtain the decrypted text.
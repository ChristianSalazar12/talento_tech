import pandas as pd

# Función para cifrar con César
def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

# Función para descifrar con César
def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)  # usar la misma función con clave negativa

# Tabla base: mensaje original y clave
base_data = [
    ("hola mundo", 3),
    ("python", 5),
    ("firewall", 8),
    ("trabajo", 2),
    ("privacidad", 7)
]

# Construcción de la tabla final
final_data = []

for original_msg, key in base_data:
    encrypted = caesar_encrypt(original_msg, key)
    decrypted = caesar_decrypt(encrypted, key)
    final_data.append({
        "mensaje_original": original_msg,
        "clave": key,
        "mensaje_cifrado": encrypted,
        "mensaje_descifrado": decrypted
    })

# Crear DataFrame con los resultados
df = pd.DataFrame(final_data)

# Mostrar tabla
print(df)

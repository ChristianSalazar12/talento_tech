
#Symmetric Key Encryption Example
#This script demonstrates how to generate a symmetric key, encrypt a message, 
# and decrypt it using the cryptography library in Python. 
#important: clone this file and the other files will genererate when you run this script.
#Author: Christian Salazar

# Libraries
from cryptography.fernet import Fernet
import os

# Function to generate symmetric key and save it to a file
def generate_key(folder):
    """Generates a symmetric key and saves it to a file."""
    key = Fernet.generate_key()
    path = os.path.join(folder, "symmetric_key.key")
    with open(path, "wb") as key_file:
        key_file.write(key)
    print(f"Clave simétrica generada y guardada en {path}")
    return path

# Function to load key from file, if it exists
def load_key(path):
    """Loads the symmetric key from a file."""
    with open(path, "rb") as key_file:
        return key_file.read()

# Encrypt message
def encrypt_message(message, key):
    """Encrypts a message using the symmetric key."""
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt message
def decrypt_message(encrypted_message, key):
    """Decrypts an encrypted message using the symmetric key."""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate key and load it
key_path = generate_key("./")
key = load_key(key_path)
print(f"Clave cargada: {key.decode()}")

# user input for message
message = input("Ingresa el mensaje que deseas cifrar:\n")

# Encrypt and save in a file txt, could be any format like json, csv, etc.
encrypted_message = encrypt_message(message, key)
print(f"Mensaje cifrado: {encrypted_message.decode()}")
with open("message.txt", "wb") as file:
    file.write(encrypted_message)

# Read and decrypt
with open("message.txt", "rb") as file:
    loaded_message = file.read()
print(loaded_message)

decrypted_message = decrypt_message(loaded_message, key)
print(f"Mensaje descifrado: {decrypted_message}")

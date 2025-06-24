import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# === Functions ===

def generate_asymmetric_keys():
    """Generates RSA key pair and saves them to PEM files"""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("Claves asimétricas generadas y guardadas.")

def load_private_key():
    """Loads the private RSA key from PEM file"""
    with open("private_key.pem", "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def load_public_key():
    """Loads the public RSA key from PEM file"""
    with open("public_key.pem", "rb") as f:
        return serialization.load_pem_public_key(f.read())

def encrypt_asymmetric(message, public_key):
    """Encrypts a message using public RSA key"""
    return public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def decrypt_asymmetric(encrypted_message, private_key):
    """Decrypts a message using private RSA key"""
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()

def sign_message(message, private_key):
    """Signs a message with the private RSA key"""
    return private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify_signature(message, signature, public_key):
    """Verifies the signature of a message using the public RSA key"""
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

# === Main Menu ===

# Generate keys (only once)
generate_asymmetric_keys()

# Load keys
private_key = load_private_key()
public_key = load_public_key()

while True:
    print("\n--- Menú ---")
    print("1. Firmar un mensaje")
    print("2. Verificar autenticidad")
    print("3. Salir")
    option = input("Seleccione una opción: ")

    if option == "1":
        message = input("Ingresa el mensaje que deseas firmar:\n")
        signature = sign_message(message, private_key)
        signature_b64 = base64.b64encode(signature).decode()
        print(f"\nFirma generada (base64):\n{signature_b64}")

    elif option == "2":
        message = input("Ingresa el mensaje original:\n")
        signature_input = input("Pega la firma (en base64):\n")
        try:
            signature_bytes = base64.b64decode(signature_input)
            is_valid = verify_signature(message, signature_bytes, public_key)
            print(f"¿El mensaje es auténtico? {'Sí' if is_valid else 'No'}")
        except Exception as e:
            print("Error al decodificar la firma o verificar el mensaje.")
            print(f"Detalles: {e}")

    elif option == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

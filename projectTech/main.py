import json
from evaluator import is_valid_password
from generator import generar_tokens_compuestos
from mnemotecnia import token_for_word
from encryption import double_encrypt
from stroke import force_stroke_cessar, force_stroke_vigenere


def registrar_consola():
    print("\n--- REGISTRO DE CONTRASEÑA ---")
    password = input("🔐 Ingresa una contraseña a evaluar: ")
    extra = input("📝 Ingresa un texto adicional (número + símbolo): ")

    # Validación
    criterios, nivel = is_valid_password(password)
    print("\n📊 Evaluación de criterios:")
    for k, v in criterios.items():
        print(f"- {k}: {'✅' if v else '❌'}")
    print(f"🔒 Nivel de seguridad: {nivel}")

    # Generación de tokens y cifrado
    tokens = generar_tokens_compuestos(password, extra)
    print("\n🧩 Tokens compuestos generados:")
    for t in tokens:
        print(f"- {t}")

    base_tokens_joins = "".join(tokens)
    key_vigenere = "segura"
    encrypted_password = double_encrypt(base_tokens_joins, key_vigenere)
    mnemotecnic_version = token_for_word(encrypted_password)

    print(f"\n🔐 Contraseña cifrada: {encrypted_password}")
    print(f"🧠 Versión mnemotécnica: {mnemotecnic_version}")

    # Guardar en archivo
    data = {"cifrada": encrypted_password, "mnemonica": mnemotecnic_version}
    with open("registro.json", "w") as f:
        json.dump(data, f)
    print("\n✅ Registro exitoso. Datos guardados en 'registro.json'.")


def login_consola():
    print("\n--- LOGIN ---")
    intento = input("🔐 Ingresa tu contraseña (cifrada o mnemotécnica): ")
    try:
        with open("registro.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: No existe 'registro.json'. Registra una contraseña primero.")
        return

    if intento == data["cifrada"] or intento == data["mnemonica"]:
        print("✅ Login exitoso. Bienvenido.")
    else:
        print("❌ Contraseña incorrecta.")


def simular_ataque():
    print("\n--- SIMULACIÓN DE ATAQUE (FORCE STROKE) ---")
    texto_cifrado = input("🔐 Ingresa el texto cifrado a descifrar: ")
    clave_objetivo = input(
        "🎯 Ingrese la clave objetivo (opcional, presiona Enter para omitir): "
    ).strip()
    clave_objetivo = clave_objetivo if clave_objetivo else None

    print("\n--- FUERZA BRUTA: CÉSAR ---")
    result_cessar = force_stroke_cessar(texto_cifrado, target=clave_objetivo)
    for shift, result in result_cessar["resultados"]:
        print(f"[Shift -{shift}] {result}")

    if result_cessar["clave_encontrada"]:
        print(f"\n✅ Clave encontrada con César: {result_cessar['clave_encontrada']}")
    else:
        print("\n❌ No se encontró la clave con César")

    print(f"⏱ Tiempo total César: {result_cessar['tiempo']:.2f} segundos")

    print("\n--- FUERZA BRUTA: VIGENÈRE ---")
    result_vigenere = force_stroke_vigenere(
        texto_cifrado, max_length=2, target=clave_objetivo
    )
    for key, result in result_vigenere["resultados"]:
        print(f"[Key: {key}] {result}")

    if result_vigenere["clave_encontrada"]:
        print(
            f"\n✅ Clave encontrada con Vigenère: {result_vigenere['clave_encontrada']}"
        )
    else:
        print("\n❌ No se encontró la clave con Vigenère")

    print(f"⏱ Tiempo total Vigenère: {result_vigenere['tiempo']:.2f} segundos")


def menu():
    while True:
        print("\n||====================================||")
        print("||    🔐 Menú Principal del Proyecto  ||")
        print("||====================================||")
        print("|| 1. Registrar nueva contraseña      ||")
        print("|| 2. Iniciar sesión                  ||")
        print("|| 3. Simular ataque (Fuerza Bruta)   ||")
        print("|| 4. Salir                           ||")
        print("||====================================||")
        print("|| Credits: Christian Salazar         ||")
        print("||====================================||")
        opcion = input("Selecciona una opción (1-4):")

        if opcion == "1":
            registrar_consola()
        elif opcion == "2":
            login_consola()
        elif opcion == "3":
            simular_ataque()
        elif opcion == "4":
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()

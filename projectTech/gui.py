import tkinter as tk
import json
import io
import sys
from tkinter import messagebox
from evaluator import is_valid_password
from generator import generar_tokens_compuestos
from encryption import double_encrypt
from mnemotecnia import token_for_word
from stroke import force_stroke_cessar, force_stroke_vigenere


def register():
    password = password_entry.get()
    extra = extra_entry.get()
    if not password or not extra:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    parameters, level = is_valid_password(password)
    label_result.config(text=f"Nivel de seguridad: {level}")

    tokens = generar_tokens_compuestos(password, extra)

    base_tokens_joins = "".join(tokens)
    key_vigenere = "segura"
    encrypted_password = double_encrypt(base_tokens_joins, key_vigenere)

    mnemotecnic_version = token_for_word(encrypted_password)
    tokens_output_text.delete(1.0, tk.END)
    tokens_output_text.insert(tk.END, "\n".join(tokens))

    label_encrypted_text.delete(1.0, tk.END)
    label_encrypted_text.insert(tk.END, encrypted_password)

    label_mnemotecnic_text.delete(1.0, tk.END)
    label_mnemotecnic_text.insert(tk.END, mnemotecnic_version)
    data = {"cifrada": encrypted_password, "mnemonica": mnemotecnic_version}
    with open("registro.json", "w") as file:
        json.dump(data, file)

    messagebox.showinfo("Registro exitoso", "Datos guardados correctamente.")


def login():
    logeo = login_entry.get()
    try:
        with open("registro.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "No se encontró el archivo de registro. Por favor, registre una contraseña primero.",
        )
        return
    if logeo == data["cifrada"] or logeo == data["mnemonica"]:
        messagebox.showinfo("Login exitoso", "Bienvenido!")
    else:
        messagebox.showerror("Error de login", "Contraseña incorrecta.")


def simulate_attack():
    encrypted_input = input_ciphered_entry.get()
    target = target_entry.get().strip()
    target = target if target else None

    if not encrypted_input:
        messagebox.showerror(
            "Error", "Por favor, ingrese un texto cifrado para descifrar."
        )
        return

    result_cessar = force_stroke_cessar(encrypted_input, target=target)
    result_vigenere = force_stroke_vigenere(
        encrypted_input, max_length=2, target=target
    )

    output = "--- FUERZA BRUTA: CÉSAR ---\n"
    for shift, resultado in result_cessar["resultados"]:
        output += f"[Shift -{shift}] {resultado}\n"

    if result_cessar["clave_encontrada"]:
        output += (
            f"\n✅ Clave encontrada con César: {result_cessar['clave_encontrada']}\n"
        )
    else:
        output += "\n❌ No se encontró la clave con César\n"

    output += f"⏱ Tiempo total César: {result_cessar['tiempo']:.2f} segundos\n\n"

    output += "--- FUERZA BRUTA: VIGENÈRE ---\n"
    for key, resultado in result_vigenere["resultados"]:
        output += f"[Key: {key}] {resultado}\n"

    if result_vigenere["clave_encontrada"]:
        output += f"\n✅ Clave encontrada con Vigenère: {result_vigenere['clave_encontrada']}\n"
    else:
        output += "\n❌ No se encontró la clave con Vigenère\n"

    output += f"⏱ Tiempo total Vigenère: {result_vigenere['tiempo']:.2f} segundos\n"

    stroke_output.delete(1.0, tk.END)
    stroke_output.insert(tk.END, output)


# =========== Interfaz =================#
window = tk.Tk()
window.title("Registro, Login y Simulación de Ataque")
window.geometry("1400x650")

# Marcos principales (alineados horizontalmente)
register_frame = tk.Frame(window, padx=20, pady=20, bg="#FAF3E0")
login_frame = tk.Frame(window, padx=20, pady=20, bg="#003366")
stroke_frame = tk.Frame(window, padx=20, pady=20, bg="#1C1C1C")  # gris oscuro

register_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
login_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
stroke_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# === Registro ===
tk.Label(
    register_frame, text="--- REGISTRO ---", font=("Arial", 14, "bold"), bg="#FAF3E0"
).pack(pady=5)
tk.Label(register_frame, text="Ingrese una Contraseña:", bg="#FAF3E0").pack()
password_entry = tk.Entry(register_frame, show="*", width=30)
password_entry.pack()

tk.Label(
    register_frame, text="Ingrese un Texto Extra (número + símbolo):", bg="#FAF3E0"
).pack()
extra_entry = tk.Entry(register_frame, width=30)
extra_entry.pack()

tk.Button(
    register_frame, text="Registrar", command=register, bg="green", fg="white"
).pack(pady=10)

label_result = tk.Label(
    register_frame, text="", font=("Arial", 12, "bold"), bg="#FAF3E0"
)
label_result.pack(pady=5)

tk.Label(register_frame, text="Tokens Compuestos:", bg="#FAF3E0").pack()
tokens_output_text = tk.Text(register_frame, width=40, height=5, bg="white", fg="black")
tokens_output_text.pack(pady=5)

label_encrypted_text = tk.Text(
    register_frame, width=40, height=2, bg="white", fg="black"
)
label_encrypted_text.pack(pady=5)

label_mnemotecnic_text = tk.Text(
    register_frame, width=40, height=2, bg="white", fg="black"
)
label_mnemotecnic_text.pack(pady=5)

# === Login ===
tk.Label(
    login_frame,
    text="--- LOGIN ---",
    font=("Arial", 14, "bold"),
    bg="#003366",
    fg="white",
).pack(pady=10)
tk.Label(
    login_frame,
    text="Ingrese su contraseña (cifrada o mnemotécnica):",
    bg="#003366",
    fg="white",
).pack()
login_entry = tk.Entry(login_frame, width=30)
login_entry.pack()

tk.Button(
    login_frame, text="Iniciar sesión", command=login, bg="blue", fg="white"
).pack(pady=20)

# =====stroke(simulation)=====
tk.Label(
    stroke_frame,
    text="--- ATAQUE (STROKE) ---",
    font=("Arial", 14, "bold"),
    bg="#1C1C1C",
    fg="white",
).pack(pady=5)
input_row = tk.Frame(stroke_frame, bg="#1C1C1C")
input_row.pack(pady=5)

tk.Label(input_row, text="Clave esperada:", bg="#1C1C1C", fg="white").pack(
    side=tk.LEFT, padx=(0, 5)
)
target_entry = tk.Entry(input_row, width=20)
target_entry.pack(side=tk.LEFT, padx=(0, 15))

tk.Label(input_row, text="Texto cifrado:", bg="#1C1C1C", fg="white").pack(
    side=tk.LEFT, padx=(0, 5)
)
input_ciphered_entry = tk.Entry(input_row, width=20)
input_ciphered_entry.pack(side=tk.LEFT)

tk.Label(
    stroke_frame,
    text="Resultados de fuerza bruta (César + Vigenère)",
    bg="#1C1C1C",
    fg="white",
).pack()

stroke_output = tk.Text(
    stroke_frame, width=60, height=25, bg="black", fg="lime", insertbackground="white"
)
stroke_output.pack(pady=10)

tk.Button(
    stroke_frame, text="Ejecutar Ataque", command=simulate_attack, bg="red", fg="white"
).pack(pady=10)

window.mainloop()

 
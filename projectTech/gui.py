import customtkinter as ctk
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

#conecta la funcion register con la interfaz en su apartado register

# ==================== FUNCIÓN REGISTRO ====================
def register():
    password = password_entry.get()
    extra = extra_entry.get()

    if not password or not extra:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    # Validación de seguridad
    parameters, level = is_valid_password(password)

    # Generar tokens
    tokens = generar_tokens_compuestos(password, extra)

    # Cifrado doble
    base_tokens_joins = "".join(tokens)
    key_vigenere = "segura"
    encrypted_password = double_encrypt(base_tokens_joins, key_vigenere)

    # Convertir a mnemotecnia
    mnemotecnic_version = token_for_word(encrypted_password)

    # Mostrar resultados en consola (output)
    output_text = (
        f"Nivel de seguridad: {level}\n"
        f"Parámetros: {parameters}\n"
    )
    output_text_tokens = (
        f"Tokens generados:\n" +
        ",".join(tokens) 
    )

    tokens_output_text_key.delete(1.0, "end")
    tokens_output_text_key.insert("end", output_text)

    tokens_output_text.delete(1.0, "end")
    tokens_output_text.insert("end", output_text_tokens)

    label_encrypted_text.delete(1.0, "end")
    label_encrypted_text.insert("end", encrypted_password)

    label_mnemotecnic_text.delete(1.0, "end")
    label_mnemotecnic_text.insert("end", mnemotecnic_version)

    # Guardar en archivo JSON
    data = {"cifrada": encrypted_password, "mnemonica": mnemotecnic_version}
    with open("registro.json", "w") as file:
        json.dump(data, file)

    messagebox.showinfo("Registro exitoso", "Datos guardados correctamente.")


# ==================== FUNCIÓN LOGIN ====================
def login():
    logeo = login_entry.get()

    try:
        with open("registro.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "No se encontró el archivo de registro.\nPor favor, realiza el registro primero.",
        )
        return

    if logeo == data["cifrada"] or logeo == data["mnemonica"]:
        messagebox.showinfo("Login exitoso", "🔓 Bienvenido!")
    else:
        messagebox.showerror("Error de login", "❌ Contraseña incorrecta.")


# ==================== FUNCIÓN SIMULACIÓN DE ATAQUE ====================
def simulate_attack():
    encrypted_input = input_ciphered_entry.get().strip()
    target = target_entry.get().strip()

    if not encrypted_input:
        messagebox.showerror(
            "Error", "Por favor, ingrese un texto cifrado para realizar el ataque."
        )
        return

    target = target if target else None

    # Fuerza bruta con César
    result_cessar = force_stroke_cessar(encrypted_input, target=target)

    # Fuerza bruta con Vigenère
    result_vigenere = force_stroke_vigenere(
        encrypted_input, max_length=2, target=target
    )

    # Construcción de salida
    output = "===== 🔍 FUERZA BRUTA: CÉSAR =====\n"
    for shift, resultado in result_cessar["resultados"]:
        output += f"[Shift -{shift}] {resultado}\n"

    if result_cessar["clave_encontrada"]:
        output += f"\n✅ Clave encontrada con César: {result_cessar['clave_encontrada']}\n"
    else:
        output += "\n❌ No se encontró la clave con César\n"

    output += f"⏱ Tiempo total César: {result_cessar['tiempo']:.2f} segundos\n\n"

    output += "===== 🔍 FUERZA BRUTA: VIGENÈRE =====\n"
    for key, resultado in result_vigenere["resultados"]:
        output += f"[Key: {key}] {resultado}\n"

    if result_vigenere["clave_encontrada"]:
        output += f"\n✅ Clave encontrada con Vigenère: {result_vigenere['clave_encontrada']}\n"
    else:
        output += "\n❌ No se encontró la clave con Vigenère\n"

    output += f"⏱ Tiempo total Vigenère: {result_vigenere['tiempo']:.2f} segundos\n"

    # Mostrar resultados en consola de ataque
    stroke_output.delete(1.0, "end")
    stroke_output.insert("end", output)


# =========== Interfaz =================#

# ========== Configuración ==========
ctk.set_appearance_mode("dark")  # "light" o "dark"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("🔐 SecurePass+")
app.geometry("1200x700")


# ========== Función para cambiar frames ==========
def mostrar_frame(frame):
    for f in [register_frame, login_frame, stroke_frame, credit_frame]:
        f.pack_forget()
    frame.pack(expand=True, fill="both", padx=20, pady=20)


# ========== Función para cambiar tema ==========
def toggle_tema():
    if tema_var.get() == "Dark":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


# ========== NavBar Lateral ==========
navbar = ctk.CTkFrame(app, width=200, corner_radius=10)
navbar.pack(side="left", fill="y", padx=10, pady=10)

ctk.CTkLabel(navbar, text="🔐 SecurePass+", font=("Arial", 22, "bold")).pack(
    pady=(15, 5), padx=10, fill="x"
)

ctk.CTkButton(
    navbar, text="Registro", command=lambda: mostrar_frame(register_frame)
).pack(pady=(15, 5), padx=10, fill="x")
ctk.CTkButton(navbar, text="Login", command=lambda: mostrar_frame(login_frame)).pack(
    pady=(15, 5), padx=10, fill="x"
)
ctk.CTkButton(
    navbar, text="Simulación", command=lambda: mostrar_frame(stroke_frame)
).pack(pady=(15, 5), padx=10, fill="x")
ctk.CTkButton(
    navbar, text="Créditos", command=lambda: mostrar_frame(credit_frame)
).pack(pady=(15, 5), padx=10, fill="x")

# Switch tema
tema_var = ctk.StringVar(value="Dark")
ctk.CTkLabel(navbar, text="Tema:").pack(pady=(20, 0))
ctk.CTkOptionMenu(
    navbar, values=["Dark", "Light"], variable=tema_var, command=lambda _: toggle_tema()
).pack(pady=5)

ctk.CTkLabel(navbar, text="").pack(expand=True)  # Espacio flexible


# ========== Frame Principal ==========
main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)


# ========== Pantalla Registro ==========
register_frame = ctk.CTkFrame(main_frame, corner_radius=15)

# Título
ctk.CTkLabel(register_frame, text="🔐 Registro", font=("Arial", 22, "bold")).pack(
    pady=10
)

# Sub-Frame que divide en dos columnas
register_content = ctk.CTkFrame(register_frame, corner_radius=10)
register_content.pack(expand=True, fill="both", padx=20, pady=20)

# ----- Lado Izquierdo: Inputs -----
input_frame = ctk.CTkFrame(register_content, corner_radius=10)
input_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(
    input_frame, text="Formulario de Registro", font=("Arial", 18, "bold")
).pack(pady=10)

ctk.CTkLabel(input_frame, text="Contraseña:").pack(pady=(15, 5), padx=10, fill="x")
password_entry = ctk.CTkEntry(input_frame, placeholder_text="Ingrese su contraseña")
password_entry.pack(pady=(15, 5), padx=10, fill="x")

ctk.CTkLabel(input_frame, text="Texto extra (número + símbolo):").pack(
    pady=(15, 5), padx=10, fill="x"
)
extra_entry = ctk.CTkEntry(input_frame, placeholder_text="Ejemplo: 9#")
extra_entry.pack(pady=(15, 5), padx=10, fill="x")

ctk.CTkButton(input_frame, text="Registrar", fg_color="#27ae60", command=register).pack(pady=15)

# ----- Lado Derecho: Consola de Salida -----
output_frame = ctk.CTkFrame(register_content, corner_radius=10)
output_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(output_frame, text="🖥️ Consola de Salida", font=("Arial", 18, "bold")).pack(
    pady=10
)
ctk.CTkLabel(output_frame, text="Nivel de seguridad:").pack(anchor="w")
tokens_output_text_key = tk.Text(output_frame, width=45, height=4, bg="#2c2c2c", fg="white")
tokens_output_text_key.pack(pady=5)

ctk.CTkLabel(output_frame, text="Tokens Generados:").pack(anchor="w")
tokens_output_text = tk.Text(output_frame, width=45, height=4, bg="#2c2c2c", fg="white")
tokens_output_text.pack(pady=5)

ctk.CTkLabel(output_frame, text="Texto Cifrado:").pack(anchor="w")
label_encrypted_text = tk.Text(
    output_frame, width=45, height=2, bg="#2c2c2c", fg="white"
)
label_encrypted_text.pack(pady=5)

ctk.CTkLabel(output_frame, text="Mnemotecnia:").pack(anchor="w")
label_mnemotecnic_text = tk.Text(
    output_frame, width=45, height=2, bg="#2c2c2c", fg="white"
)
label_mnemotecnic_text.pack(pady=5)

# ========== Pantalla Login ==========
login_frame = ctk.CTkFrame(main_frame, corner_radius=15)

ctk.CTkLabel(login_frame, text="🔑 Login", font=("Arial", 22, "bold")).pack(pady=10)

login_entry = ctk.CTkEntry(
    login_frame, placeholder_text="Ingrese su contraseña cifrada o mnemotécnica"
)
login_entry.pack(pady=10)

ctk.CTkButton(login_frame, text="Iniciar sesión", command=login).pack(pady=20)
# ========== Pantalla Simulación ==========
stroke_frame = ctk.CTkFrame(main_frame, corner_radius=15)

# Título principal
ctk.CTkLabel(
    stroke_frame, text="🚩 Simulación de Ataque", font=("Arial", 22, "bold")
).pack(pady=10)

# Sub-frame contenedor dividido en dos
stroke_content = ctk.CTkFrame(stroke_frame, corner_radius=10)
stroke_content.pack(expand=True, fill="both", padx=20, pady=20)

# ----- Lado Izquierdo: Inputs -----
input_stroke = ctk.CTkFrame(stroke_content, corner_radius=10)
input_stroke.pack(side="left", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(
    input_stroke, text="🛠️ Configuración del Ataque", font=("Arial", 18, "bold")
).pack(pady=10)

ctk.CTkLabel(input_stroke, text="Clave esperada:").pack(anchor="w")
target_entry = ctk.CTkEntry(input_stroke, placeholder_text="Clave a buscar")
target_entry.pack(pady=5, fill="x")

ctk.CTkLabel(input_stroke, text="Texto cifrado:").pack(anchor="w")
input_ciphered_entry = ctk.CTkEntry(input_stroke, placeholder_text="Texto cifrado")
input_ciphered_entry.pack(pady=5, fill="x")

ctk.CTkButton(input_stroke, text="Ejecutar Ataque", fg_color="#c0392b", command=simulate_attack).pack(pady=15)

# ----- Lado Derecho: Consola de Salida -----
output_stroke = ctk.CTkFrame(stroke_content, corner_radius=10)
output_stroke.pack(side="left", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(
    output_stroke, text="🖥️ Consola de Ataque", font=("Arial", 18, "bold")
).pack(pady=10)

stroke_output = tk.Text(
    output_stroke,
    width=70,
    height=20,
    bg="#2c2c2c",
    fg="lime",
    insertbackground="white",
)
stroke_output.pack(pady=5, fill="both", expand=True)
# ========== Pantalla Créditos ==========
credit_frame = ctk.CTkFrame(main_frame, corner_radius=15)

ctk.CTkLabel(credit_frame, text="👨‍💻 Créditos", font=("Arial", 22, "bold")).pack(
    pady=20
)
ctk.CTkLabel(
    credit_frame,
    text="Proyecto desarrollado por Christian Salazar\nIngeniería de Sistemas\nUniversidad de Nariño",
    justify="center",
).pack(pady=10)
ctk.CTkLabel(credit_frame, text="GitHub: https://github.com/tu_usuario").pack(pady=5)


# ========== Mostrar Registro por defecto ==========
mostrar_frame(register_frame)


# ========== Ejecutar ==========
app.mainloop()

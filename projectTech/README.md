# 🔐 Password Tokenizer & Encryption App

## 📚 Educational Cybersecurity Application

![Badge](https://img.shields.io/badge/Status-Development-green) 
![License](https://img.shields.io/badge/License-MIT-blue) 
![Python](https://img.shields.io/badge/Python-3.10+-yellow)

---

## ✨ **Description**

This application is designed to educate users about **password security**, **encryption techniques**, and the importance of using strong, non-vulnerable passwords. The tool allows you to:

- ✅ Evaluate the security level of passwords.
- ✅ Tokenize passwords combining random characters.
- ✅ Encrypt passwords using a **Double Encryption Algorithm** (César + Vigenère).
- ✅ Convert encrypted passwords into **mnemonic tokens** for easier remembering.
- ✅ Simulate brute-force attacks to demonstrate how weak encryptions are broken.

> **Educate. Protect. Strengthen.** — Cybersecurity starts with YOU. 🔐🧠

---

## 🎯 **Objective**

- ✔️ Build an interactive app that demonstrates the importance of strong passwords.
- ✔️ Provide practical exercises for students and users to understand encryption.
- ✔️ Simulate attacks to visualize how easily weak passwords can be compromised.

---

## 🚀 **Features**

| 🔍 Module | 🧠 Description                                        |
|------------|------------------------------------------------------|
| `Evaluator` | Analyze and score password strength.               |
| `Generator` | Tokenizes the password with extra random elements. |
| `Encryption`| Applies a **Double Encryption** (César + Vigenère).|
| `Mnemotecnia` | Converts ciphertext into human-friendly tokens.  |
| `Stroke`    | Simulates brute-force attacks (César/Vigenère).    |
| `GUI (Tkinter)` | Complete user interface for interaction.      |

---

## 🏗️ **Project Structure**
 

---

## 💻 **Technologies Used**

- 🐍 **Python 3.10+**
- 🎨 **Tkinter** – For GUI development
- 🔢 **NLTK** – Natural Language Toolkit (word corpus validation)
- 🔐 **Cryptography** – Manual algorithms for educational encryption

---

## 🧠 **How It Works**

1. **Register a Password:** Input your password + extra tokens (e.g., a symbol or number).
2. **Evaluate Strength:** See how strong your password is based on criteria.
3. **Generate Tokens:** A mix of your password and extra characters.
4. **Double Encrypt:** Combines **César** and **Vigenère** ciphers.
5. **Mnemonic Representation:** Turns the ciphertext into an easy-to-remember word-based code.
6. **Login:** Use your encrypted or mnemonic password to login.
7. **Attack Simulation:** Test how brute-force attacks can break weak passwords.

---

## 🔥 **Installation & Run Instructions**

### 🔧 Install Dependencies

1. Clone the repository:

```bash
git clone https://github.com/your-username/Password-Encryption-App.git
cd Password-Encryption-App


# Ahorcado (Hangman) Game in Python
# This is a simple implementation of the classic Hangman game where 
# the player has to guess a secret word by guessing letters one at a time. 
# The player has a limited number of incorrect guesses before (6 tries)
#author: Ing Christian Salazar

import random

def display_word(secret_word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

def draw_hangman(tries_left):
    stages = [
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |    |
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |    
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    
         |    
         |    
         |
        --------
        """
    ]
    print(stages[6 - tries_left])

def hangman():
    words = ['python', 'computadora', 'programacion', 'juego', 'ahorcado', 'hola', 'juan', 'dia']
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("¡Bienvenido al juego del Ahorcado!")

    while attempts > 0:
        print("\nPalabra: ", display_word(secret_word, guessed_letters))
        draw_hangman(attempts)
        print(f"Intentos restantes: {attempts}")
        print("Letras usadas:", ', '.join(sorted(guessed_letters)))
        letter = input("Digita otra letra : ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Por favor, digita solo una letra válida.")
            continue

        if letter in guessed_letters:
            print("Ya digitaste esta letra.")
        elif letter in secret_word:
            print("La letra digitada está en la palabra.")
            guessed_letters.append(letter)
        else:
            print("Letra incorrecta.")
            guessed_letters.append(letter)
            attempts -= 1

        if all(letter in guessed_letters for letter in secret_word):
            print("\n¡Felicidades! Adivinaste la palabra:", secret_word)
            break
    else:
        draw_hangman(0)
        print("\n¡Te quedaste sin intentos! La palabra era:", secret_word)

# Ejecutar el juego
hangman()

import random
import pyjokes
from art import tprint
from colorama import Fore, init
import emoji

def exit_bot():
    print(Fore.CYAN + "👋 Goodbye! Thanks for playing!")
    exit()

def main_menu():
    tprint("Fun-Bot")
    print(emoji.emojize("🤖 Welcome to Entertainment Fun-Bot!"))
    while True:
        print(Fore.BLUE + """
        ===== MENU =====
        1. 🎬 Recommend Movie
        2. 🎵 Recommend Music
        3. 🎮 Recommend Game
        4. 😂 Tell a Joke
        5. 🎲 Play 'Guess the Number'
        6. ✊ Play 'Rock-Paper-Scissors'
        7. ❌ Exit
        """)
        choice = input("Choose option (1-7): ")

        if choice == "7":
            exit_bot()
        else:
            print(Fore.RED + "❌ Invalid choice, try again!")

if __name__ == "__main__":
    main_menu()

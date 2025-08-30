import random
import pyjokes
from art import tprint
from colorama import Fore, init
import emoji

init(autoreset=True)  # auto reset colorama colors

def recommend_movies():
    movies = {
        "Action": ["Mad Max", "John Wick", "The Dark Knight"],
        "Comedy": ["The Mask", "Home Alone", "The Hangover"],
        "Sci-Fi": ["Inception", "Interstellar", "The Matrix"]
    }
    print(Fore.YELLOW + "Choose genre: Action / Comedy / Sci-Fi")
    genre = input("👉 ").capitalize()
    if genre in movies:
        print(Fore.CYAN + f"🎬 Recommended movie: {random.choice(movies[genre])}")
    else:
        print(Fore.RED + "❌ Genre not found!")

def recommend_music():
    music = {
        "Rock": ["AC/DC - Thunderstruck", "Nirvana - Smells Like Teen Spirit"],
        "Pop": ["Michael Jackson - Billie Jean", "Dua Lipa - Levitating"],
        "Classical": ["Beethoven - Symphony No.5", "Mozart - Eine kleine Nachtmusik"]
    }
    print(Fore.YELLOW + "Choose genre: Rock / Pop / Classical")
    genre = input("👉 ").capitalize()
    if genre in music:
        print(Fore.CYAN + f"🎵 Recommended track: {random.choice(music[genre])}")
    else:
        print(Fore.RED + "❌ Genre not found!")


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

        if choice == "1":
            recommend_movies()
        elif choice == "2":
            recommend_music()
        elif choice == "3":
            recommend_games()
        elif choice == "4":
            tell_joke()
        elif choice == "5":
            guess_number_game()
        elif choice == "6":
            rock_paper_scissors()
        elif choice == "7":
            exit_bot()
        else:
            print(Fore.RED + "❌ Invalid choice, try again!")

if __name__ == "__main__":
    main_menu()

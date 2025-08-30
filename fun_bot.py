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
        "Sci-Fi": ["Inception", "Interstellar", "The Matrix"],
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
        "Classical": ["Beethoven - Symphony No.5", "Mozart - Eine kleine Nachtmusik"],
    }
    print(Fore.YELLOW + "Choose genre: Rock / Pop / Classical")
    genre = input("👉 ").capitalize()
    if genre in music:
        print(Fore.CYAN + f"🎵 Recommended track: {random.choice(music[genre])}")
    else:
        print(Fore.RED + "❌ Genre not found!")


def recommend_games():
    games = ["Minecraft", "The Witcher 3", "Among Us", "Cyberpunk 2077"]
    print(Fore.CYAN + f"🎮 How about playing: {random.choice(games)}")


def tell_joke():
    joke = pyjokes.get_joke()
    print(Fore.GREEN + "😂 Here's a joke for you:")
    print(joke)


def guess_number_game():
    print(Fore.MAGENTA + "🎲 Guess the number (1-10)")
    number = random.randint(1, 10)
    while True:
        guess = input("Your guess: ")
        if not guess.isdigit():
            print(Fore.RED + "❌ Enter a number!")
            continue
        guess = int(guess)
        if guess == number:
            print(Fore.GREEN + "✅ Correct! You win!")
            break
        else:
            print(Fore.YELLOW + "❌ Wrong! Try again.")


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user = input("✊ Rock, 📄 Paper or ✂️ Scissors? ").lower()
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")
    if user == comp:
        print(Fore.YELLOW + "It's a draw!")
    elif (
        (user == "rock" and comp == "scissors")
        or (user == "scissors" and comp == "paper")
        or (user == "paper" and comp == "rock")
    ):
        print(Fore.GREEN + "✅ You win!")
    else:
        print(Fore.RED + "❌ You lose!")


def exit_bot():
    print(Fore.CYAN + "👋 Goodbye! Thanks for playing!")
    exit()


def main_menu():
    tprint("Fun-Bot")
    print(emoji.emojize("🤖 Welcome to Entertainment Fun-Bot!"))
    while True:
        print(
            Fore.BLUE
            + """
        ===== MENU =====
        1. 🎬 Recommend Movie
        2. 🎵 Recommend Music
        3. 🎮 Recommend Game
        4. 😂 Tell a Joke
        5. 🎲 Play 'Guess the Number'
        6. ✊ Play 'Rock-Paper-Scissors'
        7. ❌ Exit
        """
        )
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

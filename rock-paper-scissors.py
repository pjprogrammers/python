"""
🎮 Rock-Paper-Scissors Game
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python

✨ Description:
A simple command-line interface (CLI) game where you play against the computer
in the classic Rock-Paper-Scissors match.

🕹️ How to Play:
- Enter 'r' for Rock
- Enter 'p' for Paper
- Enter 's' for Scissors

The computer will pick its choice randomly, and the game will announce
if you won, lost, or tied.

💡 For Non-Programmers:
This game is like the hand game Rock-Paper-Scissors. You type your choice,
the computer picks one too, then the winner is decided by the usual rules:
Rock beats Scissors, Scissors beats Paper, Paper beats Rock.
"""

import random  # To generate random choices for the computer

# Mapping shorthand input letters to full choice names
CHOICES = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}

# Defining what each choice beats: key beats value
WIN_MAP = {
    'r': 's',  # Rock beats Scissors
    'p': 'r',  # Paper beats Rock
    's': 'p'   # Scissors beats Paper
}

def play():
    """
    Runs one round of Rock-Paper-Scissors:
    1️⃣ Prompts the user for input.
    2️⃣ Generates a random choice for the computer.
    3️⃣ Compares choices and declares the result.
    """
    user = input("Choose: 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()

    # Validate input
    if user not in CHOICES:
        return "❌ Invalid input. Please choose 'r', 'p', or 's'."

    computer = random.choice(list(CHOICES.keys()))

    print(f"\n🧑 You chose: {CHOICES[user]}")
    print(f"💻 Computer chose: {CHOICES[computer]}\n")

    if user == computer:
        return "🤝 It's a tie!"
    elif WIN_MAP[user] == computer:
        return "✅ You won!"
    else:
        return "❌ You lost!"

if __name__ == "__main__":
    print(play())

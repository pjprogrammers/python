"""
Rock Paper Scissors Game 🎮✨
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python
Description: A stylish GUI Rock Paper Scissors game with emojis,
modern design, and interactive play. ✂️📄🪨
"""

import random
from tkinter import *
from tkinter import messagebox as mg

# Define the possible choices with emojis to make UI friendly and clear
ROCK = "🪨 Rock"
PAPER = "📄 Paper"
SCISSORS = "✂️ Scissors"

def play(user_choice):
    """
    This function runs when the user clicks a button (Rock, Paper, or Scissors).
    It randomly selects the computer's choice,
    compares it with the user's choice,
    decides the result (win, lose, or tie),
    and finally shows the result in a popup message box.
    """
    # Extract the plain word without emoji for comparison
    user_plain = user_choice.split(" ")[1]

    # Computer randomly chooses one option
    computer_choice = random.choice([ROCK, PAPER, SCISSORS])
    computer_plain = computer_choice.split(" ")[1]

    # Determine the outcome
    if user_plain == computer_plain:
        # Same choice means it's a tie
        result = "It's a tie! 🤝"
    elif user_wins(user_plain, computer_plain):
        # Check if user wins based on game rules
        result = "You Won! 🎉"
    else:
        # Otherwise, user lost
        result = "You Lost! 😞"

    # Show the result with what the computer chose in a popup window
    mg.showinfo(title="Result", message=f"{result}\nThe Computer Chose: {computer_choice}")

def user_wins(player, opponent):
    """
    Helper function to check if the player's choice beats the opponent's choice.
    The game rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock
    Returns True if player wins, False otherwise.
    """
    return (player == "Rock" and opponent == "Scissors") or \
           (player == "Scissors" and opponent == "Paper") or \
           (player == "Paper" and opponent == "Rock")

# --- GUI Setup ---
window = Tk()  # Create main window
window.title("Rock Paper Scissors")  # Set window title
window.geometry("480x400")  # Set window size (width x height)
window.config(bg="#121212")  # Set background color to dark for sleek look

# Create a shadow effect for the title by placing two labels slightly offset
title_shadow = Label(window, text="🪨 Rock Paper Scissors ✂️", 
                     font=("Segoe UI", 22, "bold"), fg="#111111", bg="#121212")
title_shadow.place(x=24, y=28)  # Position shadow slightly offset for depth

title = Label(window, text="🪨 Rock Paper Scissors ✂️", 
              font=("Segoe UI", 22, "bold"), fg="#00FFFF", bg="#121212")
title.place(x=20, y=25)  # Main title label on top

# Instruction label guides user what to do
instruction = Label(window, text="Choose your weapon 👇", 
                    font=("Segoe UI", 14, "italic"), fg="#66FFFF", bg="#121212")
instruction.pack(pady=(90, 10))  # Padding to position nicely

# Frame holds the three buttons (Rock, Paper, Scissors)
frame = Frame(window, bg="#121212")
frame.pack(expand=True)  # Expand frame to fill space

# Button colors and styling for a modern look
base_color = "#1E1E1E"     # Button background color
hover_color = "#00FFFF"    # Color when mouse hovers over button
text_color = "#00FFFF"     # Button text color
active_bg = "#00CCCC"      # Button color when clicked
active_fg = "#121212"      # Text color when button is clicked

def create_fancy_button(parent, text, command):
    """
    Creates a styled button with hover effect to enhance user experience.
    - parent: the container widget
    - text: label on button (with emoji)
    - command: function to call on click
    Returns a Tkinter Button widget.
    """
    btn = Button(parent, text=text, command=command,
                 font=("Segoe UI", 18, "bold"),
                 bg=base_color, fg=text_color,
                 activebackground=active_bg, activeforeground=active_fg,
                 relief="flat", bd=0, width=10, height=3, cursor="hand2",
                 wraplength=90, justify="center")  # Wrap text for better fit
    
    # When mouse enters button, change colors to hover style
    def on_enter(e):
        btn['bg'] = hover_color
        btn['fg'] = "#121212"
    
    # When mouse leaves button, revert colors to base style
    def on_leave(e):
        btn['bg'] = base_color
        btn['fg'] = text_color
    
    # Bind hover effects to mouse events
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Create buttons for Rock, Paper, and Scissors with commands linked to play()
rock_btn = create_fancy_button(frame, ROCK, lambda: play(ROCK))
paper_btn = create_fancy_button(frame, PAPER, lambda: play(PAPER))
scissors_btn = create_fancy_button(frame, SCISSORS, lambda: play(SCISSORS))

# Arrange buttons in one row with spacing, responsive to resizing
rock_btn.grid(row=0, column=0, padx=15, pady=25, sticky="nsew")
paper_btn.grid(row=0, column=1, padx=15, pady=25, sticky="nsew")
scissors_btn.grid(row=0, column=2, padx=15, pady=25, sticky="nsew")

# Allow each column to expand equally when window resizes
for i in range(3):
    frame.grid_columnconfigure(i, weight=1)

# Footer label to encourage user
footer = Label(window, text="Good luck and have fun! 🎲", 
               font=("Segoe UI", 12), fg="#009999", bg="#121212")
footer.pack(side=BOTTOM, pady=20)

# Start the GUI event loop; window stays open and responsive
window.mainloop()

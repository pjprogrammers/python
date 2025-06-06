"""
Problem Solver GUI 🤔
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python
Description: A simple graphical app using tkinter message boxes to ask
if you have a problem and respond with friendly messages based on your answers. 😊
"""

import tkinter as tk
from tkinter import messagebox

def problem_solver_gui():
    """
    This function uses graphical message boxes to interact with the user.
    It asks if the user has a problem and whether they can solve it,
    then responds accordingly with a friendly message.
    """
    root = tk.Tk()       # Create the main tkinter window
    root.withdraw()      # Hide the main window, since we only need message boxes

    # Ask the user if they have a problem using a Yes/No dialog
    answer1 = messagebox.askquestion(title="Question", message="Do You Have A Problem? 🤨")

    if answer1 == "yes":
        # If yes, ask if they can solve it
        answer2 = messagebox.askquestion(title="Question", message="Can You Solve It? 🤔")

        if answer2 == "yes":
            # If they can solve it, show this message
            messagebox.showinfo(title="Information", message="Then Why Worry? 😊")
        else:
            # If they can't solve it, show the same comforting message
            messagebox.showinfo(title="Information", message="Then Why Worry? 😊")
    else:
        # If no problem, show the comforting message directly
        messagebox.showinfo(title="Information", message="Then Why Worry? 😊")

    root.destroy()  # Close the hidden main window after interactions are done

if __name__ == "__main__":
    problem_solver_gui()
 
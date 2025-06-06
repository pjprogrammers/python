"""
Problem Solver 🤔
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python
Description: A simple interactive script that asks if you have a problem
and guides you through friendly responses based on your answers. 😊
"""

p = print  # Shortcut for print function to keep code clean and readable

# Ask the user if they have a problem
p("Do You Have A Problem? 🤨")
# Take user input, strip spaces, and convert to lowercase for flexible input handling
n = input("Enter Yes or No ➟ ").strip().lower()

# Check the user's answer to the first question
if n == "yes":
    # If user says 'yes' they have a problem, ask if they can solve it
    p("Can You Solve It? 🤔")
    m = input("Enter Yes or No ➟ ").strip().lower()

    # Check the user's answer to the second question
    if m == "yes":
        # If they can solve it, no need to worry
        p("Then Why Worry? 😊")

    elif m == "no":
        # If they can't solve it, still no point worrying
        p("Then Why Worry? 😊")

    else:
        # If user input is not yes or no, show invalid input warning
        p("⚠️ Invalid input. Please enter Yes or No.")

elif n == "no":
    # If user says no problem, no need to worry
    p("Then Why Worry? 😊")

else:
    # If the first answer is not yes or no, show invalid input warning
    p("⚠️ Invalid input. Please enter Yes or No.")

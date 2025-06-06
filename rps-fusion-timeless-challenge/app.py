import os
from flask import Flask, render_template, request, session
import random

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.secret_key = os.environ.get('SECRET_KEY', 'fallback-dev-secret')  # Change this to a strong secret!

CHOICES = ["Rock", "Paper", "Scissors"]
WIN_CONDITIONS = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

@app.before_request
def initialize_session():
    if 'stats' not in session:
        session['stats'] = {'wins': 0, 'losses': 0, 'ties': 0}

def determine_winner(user, computer):
    if user == computer:
        session['stats']['ties'] += 1
        return "It's a tie! 🤝", "tie"
    elif WIN_CONDITIONS[user] == computer:
        session['stats']['wins'] += 1
        return "You Won! 🎉", "win"
    else:
        session['stats']['losses'] += 1
        return "You Lost! 😢", "loss"

@app.route("/", methods=["GET", "POST"])
def index():
    result = user_choice = computer_choice = None
    result_class = ""

    if request.method == "POST":
        user_choice = request.form.get("choice")
        if user_choice in CHOICES:
            computer_choice = random.choice(CHOICES)
            result, result_class = determine_winner(user_choice, computer_choice)

    return render_template(
        "index.html",
        result=result,
        user_choice=user_choice,
        computer_choice=computer_choice,
        stats=session['stats'],
        result_class=result_class
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

#for local host
#if __name__ == "__main__":
#    app.run(debug=True)
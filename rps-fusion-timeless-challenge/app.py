"""
🎮 Rock-Paper-Scissors Flask Game
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python

✨ Enhanced Features:
- Session-based score tracking
- Modern game UI with animations
- Responsive design
- Enhanced security
"""

from flask import Flask, render_template, request, session
import random

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.secret_key = 'dev-secret-key'  # Change for production!

# Game configuration
CHOICES = ["Rock", "Paper", "Scissors"]
WIN_CONDITIONS = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

@app.before_request
def initialize_session():
    """Initialize game stats in session if not exists"""
    if 'stats' not in session:
        session['stats'] = {'wins': 0, 'losses': 0, 'ties': 0}

def determine_winner(user, computer):
    """Enhanced winner determination with stats tracking"""
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
    """Main game route with enhanced logic"""
    result = user_choice = computer_choice = None
    result_class = ""
    
    if request.method == "POST":
        user_choice = request.form.get("choice")
        if user_choice in CHOICES:  # Input validation
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
    app.run(debug=True)
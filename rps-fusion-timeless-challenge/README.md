# 🎮 RPS Fusion: Timeless Challenge

Welcome to **RPS Fusion: Timeless Challenge**, a stylish and interactive Rock-Paper-Scissors game built with **Flask**.  
Challenge the computer in this classic game wrapped in a modern web UI with smooth background transitions and crisp animations.

---

## 👨‍💻 Author

- **Name:** PJ  
- **GitHub Profile:** [@pjprogrammers](https://github.com/pjprogrammers)  
- **Repository:** [Rock Paper Scissors Flask Game](https://github.com/pjprogrammers/python)

---

## 🚀 Features

- ✅ Play Rock 🪨, Paper 📄, or Scissors ✂️ against an intelligent computer opponent.
- 🎨 Clean, responsive, and modern design using HTML, CSS, and Flask templating.
- 🔄 Smooth rotation of 10 background images with seamless fade transitions.
- ⏳ Background image changes every 15 seconds for a relaxing dynamic feel.
- ⚡ Lightning-fast results displayed with fun emojis and user-friendly messages.
- 💾 Background rotation progress is saved via localStorage — your last viewed background loads on page reload.
- ☁️ Easily deployable to platforms like [Vercel](https://vercel.com) or any Flask-compatible host.

---

## 📁 Folder Structure

```bash
"RPS Fusion: Timeless Challenge"/
│
├── static/                    # Static assets like CSS and images
│   ├── style.css              # Main stylesheet
│   └── images/                # Background images (10 total)
│       ├── background1.jpg
│       ├── background2.jpg
│       ├── background3.jpg
│       ├── background4.jpg
│       ├── background5.jpg
│       ├── background6.jpg
│       ├── background7.jpg
│       ├── background8.jpg
│       ├── background9.jpg
│       └── background10.jpg
│
├── templates/                 # HTML templates
│   └── index.html             # Main game UI
│
├── app.py                     # Flask backend logic and routes
├── requirements.txt           # Python dependencies
├── vercel.json                # Optional config for Vercel deployment
└── README.md                  # Project documentation
````

---

## ⚙️ Installation & Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/pjprogrammers/python.git
   cd "RPS Fusion: Timeless Challenge"
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**

   ```bash
   flask run
   ```

5. **Open your browser** and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start playing!

---

## 🚀 Deployment

This app can be deployed easily on [Vercel](https://vercel.com), [Heroku](https://heroku.com), or any cloud platform supporting Python and Flask.

* For **Vercel** deployment, add the `vercel.json` file with proper settings (already included).
* Make sure to specify your `flask run` start command in deployment config.
* Static files and templates are correctly organized to work out-of-the-box.

---

## 🤝 Contribution Guidelines

Contributions are welcome! Whether you want to improve the UI, add new features, or fix bugs:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please follow standard Python code style and include descriptive commit messages.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

Enjoy the game and have fun challenging the timeless classic! 🪨📄✂️
— **PJ**
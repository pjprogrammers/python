# 🐍 PJ's Python Projects

Welcome to my personal collection of Python projects! This repository showcases a variety of applications, ranging from simple scripts to more complex web applications. Each project demonstrates different aspects of Python programming, including GUI development, web frameworks, and automation.

---

## 📂 Projects Overview

### 1. **RPS Fusion: Timeless Challenge**

A stylish and interactive Rock-Paper-Scissors game built with Flask. Features smooth background transitions, session-based score tracking, and a responsive modern UI.

![image](https://github.com/user-attachments/assets/22e5b48d-c428-4eaf-80dc-94de08d96d32)


[![🎮 Play RPS Fusion Now](https://img.shields.io/badge/🎮%20Play%20RPS%20Fusion%20Now-blueviolet?style=for-the-badge&logo=flask&logoColor=white)](https://rps-fusion-timeless-challenge.onrender.com)

### 2. **GUI Rock Paper Scissors**

A desktop application using Tkinter, providing a user-friendly interface for the classic game.

### 3. **Spiral Art Generator**

Generates intricate spiral patterns using Python's turtle graphics module.

### 4. **Student Grading System**

A command-line tool to input student marks and calculate final grades.

### 5. **Refined GUI Calculator**

A sleek calculator application built with Tkinter, offering basic arithmetic operations.

### 6. **Messagebox Do You Have A Problem**

A simple script that prompts the user with a message box question.

### 7. **Save A Dog Loop**

An interactive loop-based game where users save a dog from various challenges.

### 8. **Bulk Rename**

A utility script to batch rename files in a directory.

### 9. **Do You Have A Problem**

A command-line script that asks the user if they have a problem and responds accordingly.

---

## 🛠️ Technologies Used

- **Python**: The core programming language for all projects.
- **Flask**: A micro web framework used in the RPS Fusion game.
- **Tkinter**: Python's standard GUI library for desktop applications.
- **Turtle Graphics**: For generating spiral art patterns.
- **SQLite**: Used in the Student Grading System for data storage.

---

## ⚙️ Installation & Usage

To run any of these projects locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/pjprogrammers/python.git
   cd python
````

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the desired script**:

   For example, to run the RPS Fusion game:

   ```bash
   cd "rps-fusion-timeless-challenge"
   python app.py
   ```

---

## 📁 Folder Structure

```bash
python/
│
├── rps-fusion-timeless-challenge/  # Flask web application
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── requirements.txt
│
├── GUI_Rock_Paper_Scissors.py
├── spiral_art_generator.py
├── student_grading_system.py
├── refined_gui_calculator.py
├── Messagebox_Do_You_Have_A_Problem.py
├── Save_A_Dog_Loop.py
├── bulk-rename.py
├── do-you-have-a-problem.py
└── requirements.txt
```

---

## 🚀 Deployment

### RPS Fusion: Timeless Challenge Deployment on Render

**🔗 Live URL:** [https://rps-fusion-timeless-challenge.onrender.com](https://rps-fusion-timeless-challenge.onrender.com)

**Deployment Settings:**

* **Start Command:**

  ```bash
  gunicorn app:app
  ```

* **Build Command:**

  ```bash
  pip install -r requirements.txt
  ```

* **Runtime:** Python 3.11

* **Environment Variables:**

  ```
  FLASK_ENV=production
  SECRET_KEY=<your-strong-secret-key>
  ```

* **Port:** Automatically managed by Render (use `os.environ["PORT"]` in code)

---

## 🤝 Contribution Guidelines

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure your code adheres to PEP 8 standards and includes appropriate tests.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

Feel free to explore each project and contribute as you see fit. Happy coding! 🚀

````

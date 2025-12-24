# Guess_number_game
# 🎲 Number Guessing Game (Flask Web App)

A simple, interactive web-based number guessing game built using **Python**, **Flask**, **HTML**, and **CSS**. This project converts a traditional command-line Python game into a fully functional web application with session management and a responsive UI.

## 🚀 Features

- **Dynamic Gameplay:** Users can define how many rounds they want to play.
- **Session Management:** Uses Flask `session` to track scores and round progress across page reloads.
- **Instant Feedback:** Tells the user if their guess is "Too High" or "Too Low."
- **Scoreboard:** Live tracking of current round and total score.
- **Clean UI:** Styled with custom CSS for a modern look.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3
- **Tools:** Jinja2 Templating, Virtual Environment

## 📂 Project Structure

```text
guessing_game/
│
├── app.py                # Main Flask application logic
├── venv/                 # Virtual Environment (not uploaded to GitHub)
├── static/
│   └── style.css         # CSS for styling the UI
└── templates/
    ├── index.html        # Start screen (Enter rounds)
    └── game.html         # Main gameplay screen
```
# ⚙️ Installation & Setup
Follow these steps to run the project locally on your machine.

## 1. Clone the Repository
Bash

```git clone [https://github.com/YOUR_USERNAME/number-guessing-game.git](https://github.com/YOUR_USERNAME/number-guessing-game.git)```
```cd number-guessing-game```
## 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

Windows:

Bash

```python -m venv venv
venv\Scripts\activate
```
pip install flask
## 4. Run the Application
Start the Flask server.

Bash

python app.py
## 5. Play the Game
Open your web browser and navigate to: ```http://127.0.0.1:5000/```
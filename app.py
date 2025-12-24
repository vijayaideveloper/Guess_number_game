from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_game_session'  # Required for session storage

@app.route('/')
def index():
    # Clear previous game data when visiting the home page
    session.clear()
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    try:
        # Get number of rounds from the form
        rounds = int(request.form.get('rounds'))
        # Initialize session variables
        session['total_rounds'] = rounds
        session['current_round'] = 0
        session['score'] = 0
        return redirect(url_for('game'))
    except ValueError:
        return redirect(url_for('index'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    # If no game is started, go back home
    if 'total_rounds' not in session:
        return redirect(url_for('index'))

    message = None
    result_class = ""
    user_guess = None
    computer_val = None
    game_over = False

    if request.method == 'POST':
        try:
            user_guess = int(request.form.get('guess'))
            
            # Check if input is valid
            if user_guess < 1 or user_guess > 10:
                message = "Invalid Number! Please guess between 1 and 10."
                result_class = "error"
            else:
                # Generate computer's number
                computer_val = random.randint(1, 10)
                
                # Increment round
                session['current_round'] += 1

                # Game Logic
                if user_guess == computer_val:
                    session['score'] += 1
                    message = "Correct! +1 Point"
                    result_class = "success"
                elif user_guess > computer_val:
                    message = "Greater Number (Your guess was too high)"
                    result_class = "warning"
                else:
                    message = "Lesser Number (Your guess was too low)"
                    result_class = "warning"

                # Check if game is over
                if session['current_round'] >= session['total_rounds']:
                    game_over = True

        except ValueError:
            message = "Please enter a valid number."
            result_class = "error"

    return render_template('game.html', 
                           round=session['current_round'], 
                           total=session['total_rounds'], 
                           score=session['score'],
                           message=message,
                           result_class=result_class,
                           user_guess=user_guess,
                           computer_val=computer_val,
                           game_over=game_over)

if __name__ == '__main__':
    app.run(debug=True)
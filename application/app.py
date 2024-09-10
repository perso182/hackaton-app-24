from flask import Flask, render_template, request, redirect  
from fetch_quote import get_quote
from Game import *

# Now import the module


app = Flask(__name__)
game = Game(3)

@app.route('/restart')
def restart_game():
    game.restart_game()
    return redirect('/')

@app.route('/')
def index():
    if game.get_current_round() < game.get_max_rounds():
        quote = game.next_round()
        #quote_context = get_quote()
        return render_template('index.html', quote=quote, sources = ["Breaking Bad", "Stranger Things", "Game of Thrones"])
    else :
        print("End of game")
        return render_template('gameover.html', result="Score: " + str(game.get_score()))

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission
    user_answers = request.form
    #print(user_answers['source'])
    if game.check_answer_online(user_answers['source']):
        return render_template('result.html', result="Rätt! Sades av: " + game.get_author_of_quote())
    else:
        return render_template('result.html', result="Fel! Rätt svar är: " + game.get_correct_source() )

    

if __name__ == '__main__':
    app.run(debug=True)
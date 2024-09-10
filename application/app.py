from flask import Flask, render_template, request  
from fetch_quote import get_quote
from Game import *

# Now import the module


app = Flask(__name__)
game = Game(1)

@app.route('/')
def index():
    quote = game.next_round()
    #quote_context = get_quote()
    return render_template('index.html', quote=quote, sources = ["Breaking Bad", "Stranger Things", "Game of Thrones"])

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission
    user_answers = request.form
    #print(user_answers['source'])
    if game.check_answer_online(user_answers['source']):
        return render_template('result.html', result="Rätt")
    else:
        return render_template('result.html', result="Fel")

    

if __name__ == '__main__':
    app.run(debug=True)
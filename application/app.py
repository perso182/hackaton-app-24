from flask import Flask, render_template, request  
from fetch_quote import get_quote
 

# Now import the module


app = Flask(__name__)

@app.route('/')
def index():
    quote_context = get_quote()
    return render_template('index.html', quote=quote_context.quote, sources = ["Breaking Bad", "Stranger Things", "Game of Thrones"])

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission
    user_answers = request.form
    return render_template('result.html', result=user_answers)

if __name__ == '__main__':
    app.run(debug=True)
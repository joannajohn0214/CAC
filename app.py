# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import quiz_results
# from flask import request

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/advice')
def advice():
    return render_template('advice.html')

#Personality Quiz
@app.route('/quiz_answer', methods=['GET','POST'])
def quiz():
  # store the quiz answers in a dict
  # quiz_answer = request.form
  # store the outcome of the model function in a new variable
  # advice = quiz_results(quiz_answer)
  return render_template('quiz_answer.html')

@app.route('/answer', methods=['GET', 'POST'])
def answer():
  answers = request.form
  advice = quiz_results(answers)
  return render_template('result.html', answer=advice)


app.run(host='0.0.0.0', port=81, debug=True)
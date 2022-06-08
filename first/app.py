from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def roll_dice():
  return "The dice rolled: {} ".format(randint(1,6))




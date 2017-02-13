from flask import Flask
import sample
app = Flask(__name__)


@app.route('/')
def hello_world():
    text = open('huckfinn.txt', 'r')
    return sample.random_sentence(sample.histogram(text), 10)

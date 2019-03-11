from blockly import blockly
from flask import render_template


@blockly.route('/')
def home():
    return render_template('index.html')

'''
@blockly.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@restful.route('/')
def home():
    return render_template('index.html')

'''
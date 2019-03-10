from vapaa import vapaa
from flask import render_template


@vapaa.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')
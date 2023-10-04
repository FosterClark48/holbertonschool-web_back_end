#!/usr/bin/env python3
""" Basic Flask App Module """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Route for index page """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

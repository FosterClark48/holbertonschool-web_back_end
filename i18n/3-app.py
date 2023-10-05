#!/usr/bin/env python3
""" Basic Flask App Module w/ Babel setup and Locale detections """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Configuration class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply config to app
app.config.from_object(Config)

# Instantiate Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determine best match w/ supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Route for index page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

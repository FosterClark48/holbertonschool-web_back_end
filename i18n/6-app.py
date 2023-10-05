#!/usr/bin/env python3
""" Basic Flask App Module w/ Babel setup and Locale detections """
from flask import Flask, render_template, request, g
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

    # 1. Locale from URL parameters
    lang = request.args.get("locale")
    if lang and lang in app.config['LANGUAGES']:
        return lang

    # 2. Locale from user settings
    if g.get('user'):
        user_lang = g.user.get('locale')
        if user_lang and user_lang in app.config['LANGUAGES']:
            return user_lang

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

    # 4. Default locale handled by Babel once returned None


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Retrieve a user based on the login_as URL parameter """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """ Function executed before all other functions """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Route for index page """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

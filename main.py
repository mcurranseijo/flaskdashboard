from flask import Flask, render_template
import json
from spotify import Spotify
from weather import Weather
app = Flask(__name__)


@app.route('/')
def render_static():
    return render_template('index.html')


@app.route('/weather')
def weather():
    return json.dumps(Weather().state())


@app.route('/spotify')
def spotify():
    return json.dumps(Spotify().tracks())


if __name__ == '__main__':
    app.run()
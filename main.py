from flask import Flask
from flask import jsonify
from flask import render_template

from pictures_manager import load_pictures


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/pictures/')
def pictures():
    return jsonify(load_pictures())


if __name__ == "__main__":
    app.debug = True
    app.run()

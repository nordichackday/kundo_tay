from flask import Flask, jsonify, request, render_template
from flask.ext.cors import CORS, cross_origin
from datetime import datetime
import urllib2, json, time
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html");


@app.route('/ask', methods=['POST'])
def ask():
    return subprocess.Popen("/app/ask hello",
            shell=True,
            stdout=subprocess.PIPE).stdout.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

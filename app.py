from flask import Flask, request
import io, sys
import subprocess
from os import environ

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hi"

@app.route('/run/<code>', methods=['GET'])
def run(code):
    proc = subprocess.Popen(['python3', 'run.py',  code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.communicate()[0]

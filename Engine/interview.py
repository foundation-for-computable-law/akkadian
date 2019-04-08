from flask import Flask
from rules import *
from dsl import *

app = Flask(__name__)

# set FLASK_APP=interview.py
@app.route("/")
def hello():
    return Investigate(['FormW4Rules.form_w4_complete("Husband", "Wife")'])


    
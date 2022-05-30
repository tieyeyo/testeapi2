import os
import requests
from flask import Flask, request, jsonify, json

app = Flask(__name__)

login_true = 'joananew'
password_true = 'banana'


@app.route("/one/<login>/<password>")
def home(login, password=None):
    return "Login: " + login, "Password: " + password


app.run(port=5000, debug=True)

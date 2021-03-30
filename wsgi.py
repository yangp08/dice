# wsgi.py
import random
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    dice = random.randint(1,6)
    return jsonify({ 'roll': dice})

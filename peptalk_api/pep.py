#Importerar Flask klassen och Request klassen till koden
from flask import Flask, Request

# instansierar ett objekt av klassen Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "This is a test"

Export FLASK_APP=pep.py
$ app.run 
    * run on http://127.0.0.1/pep.py 
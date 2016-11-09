#Importerar Flask klassen och Request klassen till koden
from flask import Flask, request

# instansierar ett objekt av klassen Flask
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return "Testing root path. If you see this it works for %s -requests" % request.methods

@app.route("/v1/peps/", methods=['GET'])
def AllPeps():
    return "Read a file with all peps and return them as JSON"

@app.route("/v1/peps/<int:pep_id>", methods=['GET'])
def OnePep(pep_id):
    return "Read a file and get the pep with id %s" % pep_id

@app.route("/v1/peps/", methods=['POST'])
def AddPep():
    return "Adds a pep from request input data"

@app.route("/v1/peps/<int:pep_id>", methods=['PUT'])
def UpdatePep(pep_id):
    return "Update the pep with id = %s with the text: %s " % pep_id, request.data

@app.route("/v1/peps/<int:pep_id>", methods=['DELETE'])
def RemovePep(pep_id):
    return "Remove the pep from file where id = %s" % pep_id

if __name__ == "__main__":
    app.run(debug=True)
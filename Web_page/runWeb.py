from flask import Flask, jsonify, render_template, request
from getData import myJsonData as data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('_getData', methods = ['GET'])
def getData():
    return jsonify(systemData = data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
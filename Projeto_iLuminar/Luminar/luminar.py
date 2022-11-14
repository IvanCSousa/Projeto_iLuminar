from ast import Not
import json
from flask import Flask, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/", methods=["GET"])
def connect():
    return ''

@app.route("/connect", methods=["GET"])
def connect():
    return 'connect!'

@app.route("/luminar", methods=["POST"])
def create_luminar():

    solicitationJson = request.json
    
    if ("id" in solicitationJson) and ("id_sensor" in solicitationJson) and ("date" in solicitationJson):
        f = open("../logs/logs_solicitation","a")
        f.write(json.dumps(solicitationJson)+"\n")
        f.close()
        return("200")
    else:
        return("400")

if __name__ == '__main__':
    app.run(debug=True)

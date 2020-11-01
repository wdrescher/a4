import flask
import random
import json
from flask.json import jsonify, JSONDecoder


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/shuffle/', methods=['GET'])
def home():
    data: json = flask.request.get_json()
    if data is None: 
        return "Error"
    int_list = data["list_of_ints"]
    random.shuffle(int_list)
    output = {
        "shuffled_list": int_list
    }
    return jsonify(output); 

app.run(debug=True, host="0.0.0.0")
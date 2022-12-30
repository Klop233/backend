from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

dict = {
    "Klop233": "23333",
    "dad": "114514",
    "gqh": "666"
}


def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


@app.route('/get')
def route_get():  # put application's code here
    key = request.args.get("key")
    if key not in dict.keys():
        return jsonify({
            "code": 404,
            "data": ""
        })

    return jsonify({
        "code": 200,
        "data": dict[key]
    })


@app.route('/getAll')
def route_get_all():
    return jsonify({
        "code": 200,
        "data": str(dict)
    })


@app.route('/set')
def route_set():
    data = request_parse(request)
    key = data.get("key")
    value = data.get("value")
    if key is None or value is None:
        return jsonify({
            "code": "405",
            "msg": "require more parameter"
        })

    dict[key] = value
    return jsonify({
        "code": "200",
        "msg": "set successfully"
    })


@app.route('/del')
def route_del():
    data = request_parse(request)
    key = data.get("key")
    if key is None:
        return jsonify({
            "code": "405",
            "msg": "require more parameter"
        })

    dict.pop(key)
    return jsonify({
        "code": "200",
        "msg": "deleted successfully"
    })


if __name__ == '__main__':
    app.run()

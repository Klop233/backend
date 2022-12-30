from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

dict = {
    "Klop233": "23333",
    "dad": "114514"
}


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
        "data": dict
    })


if __name__ == '__main__':
    app.run()

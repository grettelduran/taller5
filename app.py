from controller.controller import Controller
from model.modelo import Player
from flask import Flask, jsonify, request, make_response, abort
import json

controller = Controller()
app = Flask(__name__)
app.config["SECRET_KEY"] = "mykey"
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False


@app.route("/")
def index():
    return "Players Application"


@app.route("/players", methods=["POST"])
def add_new_player():
    if (
        not request.json
        or not "username" in request.json
        or not "password" in request.json
        or not "name" in request.json
        or not "last_name" in request.json
        or not "email" in request.json
        or not "avatar" in request.json
    ):
        abort(400)
    result = controller.add_new_player(
        request.json.get("username"),
        request.json.get("password"),
        request.json.get("name"),
        request.json.get("last_name"),
        request.json.get("email"),
        request.json.get("avatar")
    )
    return jsonify({"result": result}), 201


@app.route("/players", methods=["GET"])
def get_all_players():
    players = controller.get_all_players()
    #genero un arreglo de jsonstrings para la visualizacion
    return jsonify({"players": [pn.to_JSON_string() for pn in players]}), 201


@app.route("/login", methods=["POST"])
def login():
    if (
        not request.json
        or not "username" in request.json
        or not "password" in request.json
    ):
        abort(400)
    result = controller.login(
        request.json.get("username"), request.json.get("password")
    )
    if result != None:
        return jsonify({"message": result}), 201
    return jsonify({"result": "An error occurred"}), 500
if __name__ == "__main__":
    app.run(debug=True)

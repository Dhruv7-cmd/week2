from flask import Blueprint, request, jsonify
from utils.validators import validate_numbers

math_bp = Blueprint("math_bp", __name__)


@math_bp.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result
    return jsonify({"result": num1 + num2})


@math_bp.route("/api/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result
    return jsonify({"result": num1 - num2})


@math_bp.route("/api/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result
    return jsonify({"result": num1 * num2})


@math_bp.route("/api/divide", methods=["POST"])
def divide():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result

    if num2 == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 422

    return jsonify({"result": num1 / num2})

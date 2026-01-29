from flask import Flask, request, jsonify

app = Flask(__name__)


def validate_numbers(data):
    if not data:
        return False, "Request body must be JSON"

    if "num1" not in data or "num2" not in data:
        return False, "num1 and num2 are required"

    num1 = data["num1"]
    num2 = data["num2"]

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return False, "num1 and num2 must be numbers"

    return True, (num1, num2)


@app.route("/")
def home():
    return "Week-2 Day-3 Math APIs running"


@app.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result
    return jsonify({"result": num1 + num2})


@app.route("/api/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result
    return jsonify({"result": num1 - num2})


@app.route("/api/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result
    return jsonify({"result": num1 * num2})


@app.route("/api/divide", methods=["POST"])
def divide():
    data = request.get_json()
    valid, result = validate_numbers(data)

    if not valid:
        return jsonify({"error": result}), 400

    num1, num2 = result

    if num2 == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 422

    return jsonify({"result": num1 / num2})


if __name__ == "__main__":
    app.run(debug=True)

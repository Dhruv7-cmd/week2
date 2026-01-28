from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Week-2 Day-2 Flask POST API is running!"

@app.route("/api/add", methods=["POST"])
def add_numbers():
    data = request.json

    num1 = data.get("num1")
    num2 = data.get("num2")

    result = num1 + num2

    return jsonify({
        "num1": num1,
        "num2": num2,
        "result": result,
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)

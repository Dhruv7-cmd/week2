from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/api/hello", methods=["GET"])
def hello_api():
    return jsonify({
        "message": "Hello from Flask API",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)

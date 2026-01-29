from flask import Flask
from routes.math_routes import math_bp

app = Flask(__name__)

app.register_blueprint(math_bp)


@app.route("/")
def home():
    return "Week-2 Day-4 Blueprint App Running"


if __name__ == "__main__":
    app.run(debug=True)

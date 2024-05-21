from flask import Flask, render_template, jsonify
import db

app = Flask(__name__)


@app.route("/ping")
def pong():
    return "pong"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/products/colour")
def api_products_colour():
    counts = db.count_products_by_colour()
    return jsonify([dict(row) for row in counts])


if __name__ == "__main__":
    app.run(debug=True)

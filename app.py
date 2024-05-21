from flask import Flask, render_template, jsonify
import db

app = Flask(__name__)


# just send back a simple string
# visit localhot:5000/ping to view
@app.route("/ping")
def pong():
    return "pong"


# send back a whole html page
# visit localhost:5000 to view
@app.route("/")
def index():
    return render_template("index.html")


# send back a json of a database table
# visit localhost:5000/api/products/colour to view
@app.route("/api/products/colour")
def api_products_colour():
    counts = db.count_products_by_colour()
    return jsonify([dict(row) for row in counts])


# run the server
if __name__ == "__main__":
    app.run(debug=True)

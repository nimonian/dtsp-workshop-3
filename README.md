# Ecommerce dashboard

Create a dashboard visualising data from a database.

## Create a virtual environment

Create the environment:

```bash
python -m venv env
```

Activate it:

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Create a server

Create `app.py` and add the following code:

```python
# app.py
from flask import Flask, render_template, jsonify
import db

app = Flask(__name__)

@app.route("/ping")
def pong():
    return "pong"


if __name__ == "__main__":
    app.run(debug=True)
```

Now run `python -m app` to run the server, and visit `localhost:5000/ping` to
see the message.

## Send back a webpage

Create `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dashboard</title>
  </head>

  <body>
    <h1>Dashboard</h1>
    <p>Welcome to the dashboard!</p>
  </body>
</html>
```

and add a new endpoint to `app.py`

```python
@app.route("/")
def index():
    return render_template("index.html")
```

Visit `localhost:5000` to view the web page.

## Connect to the database

Create the file `db.py` and add the following:

```python
import sqlite3
from pathlib import Path

DATABASE = Path().parent / "CCL_ecommerce.db"

def query_db(query, args=()):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.row_factory = sqlite3.Row  # results into dict
        result = cursor.execute(query, args).fetchall()
    return result
```

This function allows us to run queries against the database.

## Create a graph

Let's add a graph to our dashboard using [Chart.js](https://www.chartjs.org/).

First, add a function to `db.py` to get the data we need:

```python
def count_products_by_colour():
    query = """
    SELECT description, COUNT(*) as count
    FROM products
    GROUP BY description
    """

    counts = query_db(query)

    return counts
```

Second, create an endpoint to serve the data in `app.py`:

```python
from flask import Flask, render_template, jsonify
import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/products/colour")
def api_products_colour():
    counts = db.count_products_by_colour()
    return jsonify([dict(row) for row in counts])


if __name__ == "__main__":
    app.run(debug=True)
```

Third, edit `templates/index.html` to get ready to display the pie chart:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>
    <script src="../static/pieChart.js" defer></script>
    <title>Dashboard</title>
  </head>

  <body>
    <h1>Dashboard</h1>
    <p>Welcome to the dashboard!</p>
    <canvas id="pieChart"></canvas>
  </body>
</html>
```

(Notice we added two `<script>` tags and a `<canvas>` element.)

Finally, we need to create our JavaScript which fetches the data from the new
endpoint and builds the chart. In `static/pieChart.js`:

```javascript
async function main() {
  const res = await fetch('http://localhost:5000/api/products/colour')
  const data = await res.json()

  const colours = data.map(item => item.description)
  const counts = data.map(item => item.count)

  const ctx = document.getElementById('pieChart').getContext('2d')

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: colours,
      datasets: [
        {
          label: 'Product Colours',
          data: counts
        }
      ]
    },
    options: {
      responsive: true
    }
  })
}

document.addEventListener('DOMContentLoaded', main)
```

Visit `localhost:5000` to view the pie chart.

## Moving on

Explore other charts you can create with [Chart.js](https://www.chartjs.org/).
Try and extend the dashboard to add your own charts.

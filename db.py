import sqlite3
from pathlib import Path

# get an absolute path to the database
DATABASE = Path().parent / "CCL_ecommerce.db"


# helper funtion to run sql queries on the database
def query_db(query, args=()):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.row_factory = sqlite3.Row  # results into dict
        result = cursor.execute(query, args).fetchall()
    return result


def get_products():
    products = query_db("SELECT * FROM products")
    return products


def count_products_by_colour():
    query = """
    SELECT description, COUNT(*) as count
    FROM products
    GROUP BY description
    """
    counts = query_db(query)
    return counts

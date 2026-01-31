from flask import Flask, render_template, request
import mysql.connector
from model import predict_demand


app = Flask(__name__)

# MySQL connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pass123",
        database="inventory_ml"
    )

# Home route (optional)
@app.route("/")
def home():
    return "Inventory ML System is running"

# Open add product page
@app.route("/add")
def add():
    return render_template("add_product.html")

# Handle product insertion
@app.route("/add_product", methods=["POST"])
def add_product():
    product_id = request.form["product_id"]
    name = request.form["name"]
    quantity = request.form["quantity"]
    price = request.form["price"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (product_id, name, quantity, price) VALUES (%s, %s, %s, %s)",
        (product_id, name, quantity, price)
    )

    conn.commit()
    conn.close()

    return "Product added successfully"

@app.route("/products")
def view_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    return render_template("products.html", products=products)

@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/add_sale", methods=["POST"])
def add_sale():
    product_id = request.form["product_id"]
    date = request.form["date"]
    units_sold = request.form["units_sold"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO sales (product_id, date, units_sold) VALUES (%s, %s, %s)",
        (product_id, date, units_sold)
    )

    conn.commit()
    conn.close()

    return "Sales data added successfully"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None

    if request.method == "POST":
        day = int(request.form["day"])
        prediction = predict_demand(day)

    return render_template("predict.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)

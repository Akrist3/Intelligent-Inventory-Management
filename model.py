import mysql.connector
import pandas as pd
from sklearn.linear_model import LinearRegression

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pass123",
        database="inventory_ml"
    )

# Fetch sales data
def load_sales_data():
    conn = get_db_connection()
    query = "SELECT date, units_sold FROM sales"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Train ML model
def train_model():
    df = load_sales_data()

    # Convert date to numeric
    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.day

    X = df[["day"]]
    y = df["units_sold"]

    model = LinearRegression()
    model.fit(X, y)

    return model

# Predict demand
def predict_demand(day):
    model = train_model()
    prediction = model.predict([[day]])
    return int(prediction[0])


# Test ML directly
if __name__ == "__main__":
    print("Predicted demand:", predict_demand(15))

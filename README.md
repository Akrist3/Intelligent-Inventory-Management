---

# 📦 Intelligent Inventory Management System

An **Intelligent Inventory Management System** built using **Python, Flask, MySQL, and Machine Learning**.
The system helps manage inventory, track sales, and **predict future demand** using historical data.

This project demonstrates **backend development + database integration + machine learning** in a real-world scenario.

---

## 🚀 Features

* 📦 Add and manage inventory products
* 📊 View inventory dashboard
* 🧾 Record daily sales data
* 🧠 Predict future product demand using Machine Learning
* 🎨 Clean and modern web UI
* 🗄️ MySQL database integration

---

## 🛠️ Tech Stack

| Layer            | Technology           |
| ---------------- | -------------------- |
| Backend          | Python, Flask        |
| Database         | MySQL                |
| Machine Learning | Pandas, Scikit-learn |
| ML Algorithm     | Linear Regression    |
| Frontend         | HTML, CSS, Bootstrap |
| IDE              | PyCharm              |

---

## 📂 Project Structure

```
Intelligent-Inventory-Management/
│
├── app.py                # Flask application
├── model.py              # Machine Learning logic
├── db_setup.py           # Database setup
├── requirements.txt      # Python dependencies
├── index.html            # GitHub Pages landing page
│
├── templates/            # HTML templates
├── static/               # CSS and static files
└── README.md
```

---

## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Akrist3/Intelligent-Inventory-Management.git
cd Intelligent-Inventory-Management
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup MySQL Database

Create database:

```sql
CREATE DATABASE inventory_ml;
USE inventory_ml;
```

Create tables:

```sql
CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2)
);

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(50),
    date DATE,
    units_sold INT
);
```

---

### 5️⃣ Configure Database Credentials

Update MySQL credentials in:

* `app.py`
* `model.py`

```python
user="YOUR_USERNAME"
password="YOUR_PASSWORD"
```

---

### 6️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/products
```

---

## 🧠 Machine Learning Details

* **Algorithm:** Linear Regression
* **Input Feature:** Day of the month
* **Target Variable:** Units sold
* **Purpose:** Predict future inventory demand

The ML model is trained dynamically using historical sales data stored in MySQL.

---

## 🌐 Deployment Notes

* GitHub Pages is used **only for a static landing page**
* The Flask application **runs locally** due to backend and database dependencies
* This is the **standard approach for backend projects**

---

## 🔮 Future Enhancements

* Product-wise demand prediction
* LSTM / time-series forecasting
* Auto stock reordering system
* Sales & demand visualization charts
* User authentication (Admin / Staff)
* Cloud deployment (Render / AWS)

---

## 🎓 Academic & Resume Use

This project is suitable for:

* B.Tech / Final Year Project
* Mini Project
* Internship / Placement Portfolio
* Backend + ML demonstration

---

## 👨‍💻 Author

**Akrist**
B.Tech Student | Python | Machine Learning

🔗 GitHub: [https://github.com/Akrist3](https://github.com/Akrist3)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!

---

### ✅ Next, I can help you with:

1️⃣ Resume bullet points (ATS-optimized)
2️⃣ Viva questions & answers
3️⃣ Project PPT content
4️⃣ Advanced ML upgrade

Just tell me the number 🚀

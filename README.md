# dbdw-rough-2
finance
Perfect 👍 You’re building a **Finance Tracker / Portfolio Manager** with PostgreSQL + Python (Streamlit frontend, backend logic, yfinance for live prices). Here’s a clean **README.md** you can use for GitHub:

---

# 📊 Personal Finance & Portfolio Tracker

A personal finance & investment portfolio tracker built with **Python, PostgreSQL, and Streamlit**.
This app allows a user to:

* Track revenue & expenses 💰
* Manage investment accounts & assets 📈
* Record transactions (buy, sell, dividends) 🔁
* View live portfolio performance with real-time market prices (via [yfinance](https://pypi.org/project/yfinance/))

---

## 🚀 Features

### ✅ User & Account Management

* Single-user system (default user created automatically).
* Support for multiple financial accounts (Brokerage, Retirement, Crypto, etc.).

### ✅ Asset & Transaction Management

* Add new assets (stocks, bonds, crypto, commodities, real estate).
* Log transactions: Buy, Sell, Dividend.
* Tracks purchase date, quantity, price, and cost basis.

### ✅ Portfolio Performance

* Calculates holdings, average cost per unit, current value.
* Pulls **live market data** from Yahoo Finance.
* Shows gain/loss for each holding.

### ✅ Revenue & Expense Tracker

* Record business transactions (Revenue or Expense).
* Filter and sort by type, date, or amount.
* Aggregated insights:

  * Total Revenues
  * Total Expenses
  * Net Income

---

## 🛠 Tech Stack

* **Backend:** Python, psycopg2, Pandas
* **Database:** PostgreSQL
* **Frontend:** Streamlit
* **Market Data:** yfinance

---

## 📂 Project Structure

```
finance-tracker/
│── backend.py       # Database functions & portfolio logic
│── frontend.py      # Streamlit dashboard
│── requirements.txt # Python dependencies
│── schema.sql       # Database schema (tables, enums, indexes)
│── README.md        # Project documentation
```

---

## ⚡ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL Database

* Create a new database (e.g., `finance_db`).
* Run schema.sql to create tables & enums:

```bash
psql -U postgres -d finance_db -f schema.sql
```

* Update `backend.py` with your DB credentials:

```python
DB_CONFIG = {
    "dbname": "finance_db",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}
```

### 4. Run the App

```bash
streamlit run frontend.py
```

---

## 📊 Example Dashboard

* Portfolio summary with **current prices & gain/loss**.
* Revenue vs Expense overview.
* Net Income insights.

---

## 🧩 Future Improvements

* Multi-user support.
* Scheduled price updates & historical charts.
* Export reports (PDF/Excel).
* Budgeting & goal tracking.

---

## 📜 License

MIT License – free to use & modify.

---

👉 Do you also want me to create a **requirements.txt** for your repo with the correct dependencies (`streamlit, psycopg2, pandas, yfinance`)?

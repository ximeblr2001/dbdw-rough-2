import streamlit as st
import pandas as pd
from backend import get_transactions, add_transaction, update_transaction, delete_transaction, get_aggregates

st.title("💰 Finance: Revenue & Expense Tracker")

# Transaction Filter
filter_type = st.selectbox("Filter by Type", options=["All", "Revenue", "Expense"])
sort_by = st.selectbox("Sort by", options=["transaction_date", "amount"])
ascending = st.radio("Sort Order", options=["Ascending", "Descending"]) == "Ascending"

# Fetch and Display Transactions
df = get_transactions(
    filter_type=None if filter_type == "All" else filter_type,
    sort_by=sort_by,
    ascending=ascending
)
st.dataframe(df)

# Aggregation Metrics
total_transactions, total_revenue, total_expense, avg_amount, min_amount, max_amount = get_aggregates()

st.subheader("📊 Business Insights")
col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", total_transactions)
col2.metric("Total Revenue", f"₹{total_revenue:.2f}")
col3.metric("Total Expense", f"₹{total_expense:.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Average Amount", f"₹{avg_amount:.2f}")
col5.metric("Min Amount", f"₹{min_amount:.2f}")
col6.metric("Max Amount", f"₹{max_amount:.2f}")

net_income = total_revenue - total_expense
st.success(f"🧮 Net Income: ₹{net_income:.2f}")

# Add Transaction
st.subheader("➕ Add New Transaction")
with st.form("add_form"):
    transaction_id = st.text_input("Transaction ID")
    transaction_date = st.date_input("Date")
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0)
    type_ = st.selectbox("Type", options=["Revenue", "Expense"])
    submitted = st.form_submit_button("Add")
    if submitted:
        add_transaction(transaction_id, transaction_date, description, amount, type_)
        st.success("Transaction added!")

# Delete Transaction
st.subheader("🗑️ Delete Transaction")
delete_id = st.text_input("Enter Transaction ID to Delete")
if st.button("Delete"):
    delete_transaction(delete_id)
    st.warning("Transaction deleted!")

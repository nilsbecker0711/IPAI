import streamlit as st
import time
import numpy as np
import pandas as pd

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

data = pd.DataFrame([[0.0]], columns=["My bank account"])
chart = st.line_chart(data)
discount_rate = st.sidebar.slider("Discount rate", 0, 100, 2)
nums = st.text_input("Cash flow", value="-150 50 50 50 50 50 50 50 50 50 50 50")

cash = [float(y) for y in nums.split()]

def cash_flow(C, discount_rate, iteration):
    s = 0
    for i in range(iteration):
        s += C[i] / ((1. + discount_rate / 100.0) ** i)
    return s


for i in range(0, 10):
    status_text.text(f"{i+1} of 10 years complete")
    row = pd.DataFrame([[cash_flow(cash, discount_rate, i)]], columns=["My bank account"])
    data = data.append(row, ignore_index=True)
    print(data)
    chart.line_chart(data)
    progress_bar.progress(i * 10)
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
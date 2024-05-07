import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Membaca database
data = pd.read_csv("tips.csv")

# Menampilkan Teks 
st.subheader("Muhammad Asyam Thoriq Taufiqurahman")
st.subheader("21082010155")

# Scatter plot
plt.scatter(data['day'], data['tip'])
plt.title("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')
st.pyplot(plt)

# Line Plot
plt.title("Line Plot")
fig, ax = plt.subplots(figsize=(10, 6))
line_plot = sns.lineplot(data=data.drop(['total_bill'], axis=1), ax=ax)
st.pyplot(fig)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/sendy-ty/Submission-/refs/heads/main/dataset/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/sendy-ty/Submission-/refs/heads/main/dataset/hour.csv")

# Preprocessing
day_df.rename(columns={"dteday": "date", "yr": "year", "mnth": "month", "hum": "humidity", "cnt": "total_rentals"}, inplace=True)
hour_df.rename(columns={"dteday": "date", "yr": "year", "mnth": "month", "hum": "humidity", "cnt": "total_rentals"}, inplace=True)

day_df["date"] = pd.to_datetime(day_df["date"])
hour_df["Date"] = pd.to_datetime(hour_df["Date"])

# Streamlit Sidebar Filters
st.sidebar.header("Filter data")
start_date, end_date = st.sidebar.date_input("Select date range", [day_df["Date"].min(), day_df["Date"].max()])
filtered_df = day_df[(day_df["Date"] >= pd.to_datetime(start_date)) & (day_df["Date"] <= pd.to_datetime(end_date))]

# Dashboard Title
st.title("Bike Sharing Dashboard")

# Total Rentals Metric
st.metric("Total Rentals", value=filtered_df["total_rentals"].sum())

# Daily Rentals Line Chart
st.subheader("Daily Rentals Trend")
fig, ax = plt.subplots(figsize=(12, 6))
ax.Plot(filtered_df["Date"], filtered_df["total_rentals"], Marker="o", Color="Blue")
ax.set_xlabel("Date")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# Hourly Rentals Bar Chart
st.subheader("Hourly Rentals")
hourly_avg = hour_df.groupby("HR")["total_rentals"].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x="HR", y="total_rentals", data=hourly_avg, palette="Blues", ax=ax)
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Rentals")
st.pyplot(fig)

st.caption("© 2025 Bike Sharing Analysis")

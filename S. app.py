import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("🌊 Smart Water & Energy Management Prototype")

# --- Simulation settings ---
days = 30
pump_capacity = 200        # liters per hour
diesel_per_hour = 2        # liters per hour
co2_per_liter = 0.00268    # tons CO2 per liter of diesel
carbon_price = 15          # $ per ton CO2

# --- Random simulation data ---
sun_hours = np.random.uniform(4, 6, days)
daily_demand = np.random.uniform(800, 1200, days)

# --- Calculate outputs ---
results = []
for day in range(days):
    sunlight = sun_hours[day]
    demand = daily_demand[day]
    solar_output = min(demand, sunlight * pump_capacity)
    diesel_needed = max(0, demand - solar_output)
    diesel_hours = diesel_needed / pump_capacity
    diesel_used = diesel_hours * diesel_per_hour
    co2_emission = diesel_used * co2_per_liter
    carbon_value = co2_emission * carbon_price
    results.append({
        "Day": day + 1,
        "Demand (L)": round(demand, 2),
        "Solar Output (L)": round(solar_output, 2),
        "Diesel Used (L)": round(diesel_used, 2)
    })

df = pd.DataFrame(results)

# --- Display last 7 days only for simplicity ---
st.subheader("Last 7 Days Simulation")
st.dataframe(df.tail(7))

# --- Predict next day's demand ---
X = df["Day"].values.reshape(-1, 1)
y = df["Demand (L)"].values
model = LinearRegression()
model.fit(X, y)
predicted_demand = model.predict([[days + 1]])[0]
st.markdown(f"### 🔮 Predicted water demand for Day {days + 1}: {predicted_demand:.2f} L")

# --- Simple plot ---
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["Day"], df["Demand (L)"], label="Demand (L)", marker='o')
ax.plot(df["Day"], df["Solar Output (L)"], label="Solar Output (L)", marker='x')
ax.plot(df["Day"], df["Diesel Used (L)"], label="Diesel Used (L)", marker='s')
ax.scatter(days + 1, predicted_demand, color="purple", label="Predicted Demand", s=80)
ax.set_xlabel("Day")
ax.set_ylabel("Liters")
ax.set_title("Water Demand & Production - 30 Days Simulation")
ax.legend()
ax.grid(True)
st.pyplot(fig)

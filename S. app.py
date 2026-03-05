# smart_water_system.py
# 🌊 Smart Water & Energy Management System - Prototype Simulation
# Author: Salim Altrymy
# Purpose: Simulate solar-diesel water pumping, CO2 accounting, and demand prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ===============================
# 1️⃣ Setup Simulation Data
# ===============================
days = 30  # simulate one month
pump_capacity = 200  # liters/hour
diesel_per_hour = 2  # liters/hour
co2_per_liter = 0.00268  # ton CO2 per liter of diesel
carbon_price = 15  # $ per ton CO2

# Randomized sample data (prototype simulation)
sun_hours = np.random.uniform(4, 6, days)
daily_demand = np.random.uniform(800, 1200, days)

# ===============================
# 2️⃣ Daily Pump Simulation
# ===============================
results = []

for day in range(days):
    sunlight = sun_hours[day]
    demand = daily_demand[day]
    
    # Solar production
    solar_output = min(demand, sunlight * pump_capacity)
    
    # Diesel required for remaining demand
    diesel_needed = max(0, demand - solar_output)
    diesel_hours = diesel_needed / pump_capacity
    diesel_used = diesel_hours * diesel_per_hour
    
    # CO2 and carbon financial value
    co2_emission = diesel_used * co2_per_liter
    carbon_value = co2_emission * carbon_price
    
    results.append({
        "Day": day + 1,
        "Demand(L)": round(demand,2),
        "Solar Output(L)": round(solar_output,2),
        "Diesel Used(L)": round(diesel_used,2),
        "CO2 Emission(Ton)": round(co2_emission,4),
        "Carbon Value($)": round(carbon_value,2)
    })

df = pd.DataFrame(results)
df.to_csv("simulation_results.csv", index=False)  # save CSV for GitHub

# ===============================
# 3️⃣ Predict Next Day Demand
# ===============================
X = df["Day"].values.reshape(-1,1)
y = df["Demand(L)"].values

model = LinearRegression()
model.fit(X, y)

next_day = np.array([[days + 1]])
predicted_demand = model.predict(next_day)[0]

# ===============================
# 4️⃣ Print Summary
# ===============================
print(df)
print("\n=== 30-Day Summary ===")
print(f"Total Diesel Used(L): {round(df['Diesel Used(L)'].sum(),2)}")
print(f"Total CO2 Emission(Ton): {round(df['CO2 Emission(Ton)'].sum(),2)}")
print(f"Total Carbon Value($): {round(df['Carbon Value($)'].sum(),2)}")
print(f"Predicted Water Demand for Day {days+1}: {round(predicted_demand,2)} L")

# ===============================
# 5️⃣ Visualization
# ===============================
plt.figure(figsize=(12,6))
plt.plot(df["Day"], df["Demand(L)"], label="Actual Demand (L)", color="blue", marker='o')
plt.plot(df["Day"], df["Solar Output(L)"], label="Solar Output (L)", color="green", marker='x')
plt.plot(df["Day"], df["Diesel Used(L)"], label="Diesel Used (L)", color="red", marker='s')
plt.scatter(days+1, predicted_demand, color="purple", label="Predicted Demand", s=100)
plt.title("Water Production & Diesel Use - 30 Days Simulation + Prediction")
plt.xlabel("Day")
plt.ylabel("Liters")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12,6))
plt.bar(df["Day"], df["CO2 Emission(Ton)"], color="orange")
plt.title("Daily CO2 Emission (Ton) from Diesel Use")
plt.xlabel("Day")
plt.ylabel("CO2 Emission (Ton)")
plt.grid(axis='y')
plt.show()

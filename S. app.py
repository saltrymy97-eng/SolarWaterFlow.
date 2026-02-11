# SolarWaterFlow.
"Retrofitting global water assets with AI to transform existing pumps into smart, self-funding, and sustainable networks."


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------
# AI Prediction Functions
# ----------------------------------

def predict_solar_energy(temperature, sunlight_hours):
    """Predict solar energy based on temperature and sunlight hours."""
    return 0.5 * sunlight_hours * temperature

def predict_water_demand(temperature, population):
    """Predict water demand based on temperature and population."""
    return 0.3 * population * temperature

def system_recommendation(solar_energy, water_demand):
    """AI Decision Agent logic."""
    if solar_energy > (water_demand * 0.01):
        return "✅ System Decision: Solar energy is SUFFICIENT to meet water demand."
    else:
        return "⚠️ System Decision: Energy is INSUFFICIENT. Consider battery storage or demand reduction."

# ----------------------------------
# Streamlit UI Configuration
# ----------------------------------
st.set_page_config(page_title="SolarWaterFlow AI", layout="centered")
st.title("🌞💧 Smart Water & Solar Management")

st.markdown("""
This AI-driven system evaluates **Solar Energy Production** vs **Water Demand** to provide intelligent recommendations for sustainable resource management.
""")

# ----------------------------------
# Sidebar Inputs
# ----------------------------------
st.sidebar.header("System Parameters")
temperature = st.sidebar.slider("🌡️ Ambient Temperature (°C)", 0, 45, 25)
sunlight_hours = st.sidebar.slider("☀️ Sunlight Hours/Day", 0, 12, 8)
population = st.sidebar.slider("👥 Population Size", 100, 10000, 1000, step=100)

# ----------------------------------
# Execution & Analysis
# ----------------------------------
if st.button("🔍 Run AI Analysis"):
    solar_energy = predict_solar_energy(temperature, sunlight_hours)
    water_demand = predict_water_demand(temperature, population)
    decision = system_recommendation(solar_energy, water_demand)

    st.write("---")
    
    # Results Display using Metrics
    st.subheader("📊 AI Analytics")
    col1, col2 = st.columns(2)
    col1.metric("Solar Production", f"{solar_energy:.2f} kWh")
    col2.metric("Water Demand", f"{water_demand:.2f} L/day")

    # AI Decision Output
    st.subheader("🧠 AI Decision Agent")
    if "SUFFICIENT" in decision:
        st.success(decision)
    else:
        st.warning(decision)

    # ----------------------------------
    # Visualizations
    # ----------------------------------
    st.write("---")
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # Solar Chart
    ax[0].bar(["Solar Energy"], [solar_energy], color='#FFD700')
    ax[0].set_title("Energy (kWh)")
    ax[0].set_ylim(0, max(solar_energy * 1.2, 10))

    # Water Chart
    ax[1].bar(["Water Demand"], [water_demand], color='#1E90FF')
    ax[1].set_title("Water Demand (Liters)")
    ax[1].set_ylim(0, max(water_demand * 1.2, 100))

    st.pyplot(fig)
    

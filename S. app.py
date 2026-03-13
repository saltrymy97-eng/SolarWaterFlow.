import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="H2O-Smart Carbon Tracker", layout="wide")

st.title("🌊 Project H₂O-Smart: Sensor Efficiency & Carbon Report")
st.markdown("---")

# --- 1. Simulation of Sensor Percentages ---
# In a real scenario, these values come from your hardware sensors
def get_sensor_percentages():
    return {
        "solar_efficiency": 92,    # % of max sun intensity
        "water_production": 85,    # % of max flow rate
        "electrical_load": 60,     # % of safe motor capacity
        "diesel_inventory": 45,    # % of fuel remaining
        "reservoir_level": 78      # % of tank capacity
    }

data = get_sensor_percentages()

# --- 2. Visual Sensor Gauges (Progress Bars) ---
st.subheader("📊 Individual Sensor Performance (%)")
col1, col2 = st.columns(2)

with col1:
    st.write(f"☀️ **Solar Intensity:** {data['solar_efficiency']}%")
    st.progress(data['solar_efficiency'] / 100)
    
    st.write(f"💧 **Flow Production:** {data['water_production']}%")
    st.progress(data['water_production'] / 100)
    
    st.write(f"⚡ **Motor Load Health:** {data['electrical_load']}%")
    st.progress(data['electrical_load'] / 100)

with col2:
    st.write(f"⛽ **Diesel Inventory:** {data['diesel_inventory']}%")
    st.progress(data['diesel_inventory'] / 100)
    
    st.write(f"🌊 **Reservoir Level:** {data['reservoir_level']}%")
    st.progress(data['reservoir_level'] / 100)

st.markdown("---")

# --- 3. Carbon Emission Logic (Diesel to CO2) ---
st.subheader("🌿 Environmental Impact Analysis")

# Logic: If solar is high, we save diesel. 
# Let's assume 15 Liters were saved today.
liters_saved = 15.0 
CO2_FACTOR = 2.68 # 1 Liter of Diesel = 2.68 kg of CO2
co2_avoided_kg = liters_saved * CO2_FACTOR

c1, c2 = st.columns(2)
with c1:
    st.metric(label="⛽ Diesel Saved", value=f"{liters_saved} Liters")
with c2:
    st.metric(label="🌱 CO₂ Emissions Avoided", value=f"{co2_avoided_kg:.2f} kg")

# --- 4. Final Functional Audit Report ---
st.markdown("---")
if st.button("Generate Final Sensor Report"):
    st.header("📄 Official System Status Report")
    
    report_text = f"""
    - **Solar Sensor:** Operating at **{data['solar_efficiency']}%**. Energy is sufficient to bypass the generator.
    - **Water Flow Sensor:** Confirmed **{data['water_production']}%** efficiency. Delivery pipes are clear and stable.
    - **Power Sensor:** Current load is at **{data['electrical_load']}%**. Motor is running within safe limits with no faults.
    - **Diesel Sensor:** Fuel stock is at **{data['diesel_inventory']}%**. Backup power is ready for night operations.
    - **Water Level Sensor:** Reservoir is **{data['reservoir_level']}%** full. Water security for the community is high.
    
    **Carbon Statement:**
    By utilizing solar energy, the system avoided the combustion of {liters_saved}L of diesel, 
    preventing **{co2_avoided_kg:.2f} kg of CO₂** from entering the atmosphere.
    """
    st.success("Report Generated Successfully!")
    st.write(report_text)


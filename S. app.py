import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="H2O-Smart Carbon Tracker", layout="wide")

st.title("🌊 Project H₂O-Smart: Sensor Efficiency & Carbon Report")
st.markdown("---")

# --- 1. Sensor Readings Simulation ---
def get_sensor_readings():
    return {
        "solar_efficiency": 92,    # % of available solar energy
        "water_flow": 85,          # % of max water flow
        "motor_load": 60,          # % of current motor load
        "diesel_level": 45,        # % of diesel fuel remaining
        "reservoir_level": 78      # % of reservoir water level
    }

data = get_sensor_readings()

# --- 2. Sensor Limits for Alerts ---
LIMITS = {
    "motor_load": 80,
    "diesel_level": 20,
    "water_flow": 50,
    "reservoir_level": 30  # below 30% considered low
}

# --- 3. Visual Sensor Gauges ---
st.subheader("📊 Sensor Status & Efficiency (%)")
col1, col2 = st.columns(2)

with col1:
    st.write(f"☀️ **Solar Efficiency:** {data['solar_efficiency']}%")
    st.progress(data['solar_efficiency'] / 100)

    st.write(f"💧 **Water Flow:** {data['water_flow']}%")
    st.progress(data['water_flow'] / 100)
    if data['water_flow'] < LIMITS['water_flow']:
        st.warning("⚠️ Water flow is below optimal level!")

    st.write(f"⚡ **Motor Load:** {data['motor_load']}%")
    st.progress(data['motor_load'] / 100)
    if data['motor_load'] > LIMITS['motor_load']:
        st.error("❌ Motor load is too high! Check the system.")

with col2:
    st.write(f"⛽ **Diesel Level:** {data['diesel_level']}%")
    st.progress(data['diesel_level'] / 100)
    if data['diesel_level'] < LIMITS['diesel_level']:
        st.warning("⚠️ Diesel running low! Refill soon.")

    st.write(f"🌊 **Reservoir Level:** {data['reservoir_level']}%")
    st.progress(data['reservoir_level'] / 100)
    if data['reservoir_level'] < LIMITS['reservoir_level']:
        st.warning("⚠️ Reservoir water level low! Refill required.")

# --- 4. Environmental Impact (Carbon) ---
st.markdown("---")
st.subheader("🌿 Environmental Impact Analysis")

daily_diesel_saved = round((data['solar_efficiency']/100)*10, 2)  # e.g., solar % * 10 liters saved
CO2_FACTOR = 2.68  # 1 liter of diesel = 2.68 kg CO2
daily_CO2_avoided = daily_diesel_saved * CO2_FACTOR
monthly_diesel_saved = daily_diesel_saved * 30
monthly_CO2_avoided = daily_CO2_avoided * 30

c1, c2 = st.columns(2)
with c1:
    st.metric(label="⛽ Daily Diesel Saved", value=f"{daily_diesel_saved} L")
    st.metric(label="⛽ Estimated Monthly Diesel Saved", value=f"{monthly_diesel_saved:.2f} L")
with c2:
    st.metric(label="🌱 Daily CO₂ Avoided", value=f"{daily_CO2_avoided:.2f} kg")
    st.metric(label="🌱 Estimated Monthly CO₂ Avoided", value=f"{monthly_CO2_avoided:.2f} kg")

# --- 5. Final System Report ---
st.markdown("---")
if st.button("Generate Final Sensor Report"):
    st.header("📄 Official H₂O-Smart System Report")

    report_text = f"""
    - ☀️ **Solar Sensor:** Operating at {data['solar_efficiency']}%. Solar energy is utilized efficiently.
    - 💧 **Water Flow Sensor:** Current flow at {data['water_flow']}%. {'Flow is below optimal!' if data['water_flow'] < LIMITS['water_flow'] else 'Flow is stable.'}
    - ⚡ **Motor Load Sensor:** Load at {data['motor_load']}%. {'High load detected!' if data['motor_load'] > LIMITS['motor_load'] else 'Motor operating safely.'}
    - ⛽ **Diesel Sensor:** Fuel at {data['diesel_level']}%. {'Low fuel warning!' if data['diesel_level'] < LIMITS['diesel_level'] else 'Fuel level sufficient.'}
    - 🌊 **Reservoir Level Sensor:** Reservoir at {data['reservoir_level']}%. {'Low water warning!' if data['reservoir_level'] < LIMITS['reservoir_level'] else 'Water level sufficient.'}

    **Environmental Impact Statement:**
    Daily diesel saved: {daily_diesel_saved} L → CO₂ avoided: {daily_CO2_avoided:.2f} kg
    Estimated monthly diesel saved: {monthly_diesel_saved:.2f} L → CO₂ avoided monthly: {monthly_CO2_avoided:.2f} kg
    """
    st.success("✅ Report Generated Successfully!")
    st.write(report_text)

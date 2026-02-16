import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq

# 1. Secure AI Configuration (Using Streamlit Secrets)
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except Exception:
    st.error("❌ API Key not found! Please add 'GROQ_API_KEY' to your Streamlit Secrets.")
    st.stop()

class WaterAI:
    def __init__(self, temp, sun, pop, diesel):
        self.temp = temp
        self.sun = sun
        self.pop = pop
        self.diesel = diesel

    def analyze(self):
        solar_gen = 0.5 * self.sun * self.temp
        water_req = 0.3 * self.pop * self.temp
        energy_needed = water_req * 0.05
        diesel_saved = energy_needed * 0.4
        cash_saved = diesel_saved * self.diesel
        co2_offset = diesel_saved * 2.68
        return {
            "solar": solar_gen,
            "demand": water_req,
            "cash": cash_saved,
            "co2": co2_offset
        }

    def get_advice(self, data):
        prompt = f"Data: Solar {data['solar']:.1f}kWh, Water {data['demand']:.1f}L, Savings ${data['cash']:.2f}. Task: 3 strategic business points in English."
        try:
            chat = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama3-8b-8192")
            return chat.choices[0].message.content
        except:
            return "AI Consultant is analyzing the data..."

# 2. UI Layout
st.set_page_config(page_title="SolarWaterFlow AI", layout="wide")
st.title("🌞💧 SolarWaterFlow: AI Strategic Agent")

# Sidebar Controls
st.sidebar.header("System Parameters")
t = st.sidebar.slider("Ambient Temp (°C)", 0, 50, 30)
s = st.sidebar.slider("Sunlight Hours", 0, 14, 10)
p = st.sidebar.slider("Population", 100, 10000, 2000)
d = st.sidebar.number_input("Diesel Price ($/L)", value=1.2)

# Execution
agent = WaterAI(t, s, p, d)
res = agent.analyze()

# Metrics Display
col1, col2, col3, col4 = st.columns(4)
col1.metric("Solar Gen", f"{res['solar']:.1f} kWh")
col2.metric("Water Demand", f"{res['demand']:.0f} L")
col3.metric("Money Saved", f"${res['cash']:.2f}")
col4.metric("CO2 Saved", f"{res['co2']:.1f} kg")

# AI Insights
st.subheader("🤖 AI Strategic Insights")
st.info(agent.get_advice(res))

# Charts
st.subheader("📊 Performance Analytics")
fig, ax = plt.subplots(figsize=(8, 3))
ax.bar(['Energy Supply', 'Water Energy Need'], [res['solar'], res['demand']*0.05], color=['#FFD700', '#1E90FF'])
st.pyplot(fig)

st.divider()
st.caption("Developed by Salim Al-Radhwi | Secure AI & Accounting Integration")
    

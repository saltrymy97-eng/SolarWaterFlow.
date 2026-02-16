import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq

# --- SECURE CONFIGURATION ---
try:
    # Safe: No key visible here
    key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=key)
except Exception:
    st.error("❌ Security Error: API Key not found in Secrets. Please add it to your Streamlit dashboard.")
    st.stop()

class SolarWaterAgent:
    def __init__(self, temp, sun, pop, diesel):
        self.temp, self.sun, self.pop, self.diesel = temp, sun, pop, diesel

    def calculate(self):
        solar_gen = 0.5 * self.sun * self.temp
        water_req = 0.3 * self.pop * self.temp
        money_saved = (water_req * 0.05 * 0.4) * self.diesel
        return {"solar": solar_gen, "demand": water_req, "savings": money_saved}

    def get_ai_insight(self, data):
        prompt = f"Solar: {data['solar']:.1f}kWh, Water: {data['demand']:.0f}L, Savings: ${data['savings']:.2f}. Give 3 strategic bullet points in English."
        try:
            chat = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama3-8b-8192")
            return chat.choices[0].message.content
        except: return "AI Agent is offline."

# --- UI Interface ---
st.set_page_config(page_title="SolarFlow AI", layout="wide")
st.title("⚡ SolarWaterFlow: AI Strategic Agent")

t = st.sidebar.slider("Temperature (°C)", 0, 50, 30)
s = st.sidebar.slider("Sun Hours", 0, 14, 10)
p = st.sidebar.slider("Population", 100, 10000, 2500)
d = st.sidebar.number_input("Diesel Price ($/L)", value=1.20)

agent = SolarWaterAgent(t, s, p, d)
res = agent.calculate()

c1, c2, c3 = st.columns(3)
c1.metric("Solar Output", f"{res['solar']:.1f} kWh")
c2.metric("Water Demand", f"{res['demand']:.0f} L")
c3.metric("Daily Savings", f"${res['savings']:.2f}")

st.subheader("🤖 AI Strategic Advice")
st.info(agent.get_ai_insight(res))

st.caption("Developed by Salim Al-Radhwi | Secure AI Integration")
        

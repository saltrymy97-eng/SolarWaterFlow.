import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq

# ----------------------------------
# 🔑 Groq AI Agent Configuration
# --------------------------------- = "
client = Groq(api_key=GROQ_API_KEY)

class SolarWaterAgent:
    def __init__(self, temp, sun_hours, pop, diesel_price):
        self.temp = temp
        self.sun_hours = sun_hours
        self.pop = pop
        self.diesel_price = diesel_price

    def calculate_metrics(self):
        solar_gen = 0.5 * self.sun_hours * self.temp
        water_req = 0.3 * self.pop * self.temp
        
        # Financial Logic
        energy_needed_kwh = water_req * 0.05
        diesel_saved_liters = energy_needed_kwh * 0.4
        money_saved = diesel_saved_liters * self.diesel_price
        carbon_offset = diesel_saved_liters * 2.68 
        
        return {
            "solar": solar_gen,
            "demand": water_req,
            "savings": money_saved,
            "carbon": carbon_offset,
            "diesel_liters": diesel_saved_liters
        }

    def get_ai_advisor_response(self, data):
        prompt = f"""
        Role: Senior Financial & Energy Consultant.
        Data: Solar {data['solar']:.1f}kWh, Water {data['demand']:.1f}L, Savings ${data['savings']:.2f}, CO2 {data['carbon']:.1f}kg.
        Context: Yemen water crisis and renewable energy transition.
        Task: Provide 3-4 professional strategic bullet points on ROI and efficiency.
        Language: English.
        """
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"AI Advisor is temporarily offline. System is running on local logic."

# ----------------------------------
# 🎨 Professional Dashboard UI
# ----------------------------------
st.set_page_config(page_title="SolarWaterFlow AI", layout="wide", page_icon="⚡")

# Fixed CSS injection
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ SolarWaterFlow: Advanced AI Agent")
st.markdown("#### *Empowering sustainable water networks with Llama 3 & Groq LPU™*")

# Sidebar
st.sidebar.header("📊 System Parameters")
temp = st.sidebar.slider("Ambient Temperature (°C)", 0, 50, 30)
sun = st.sidebar.slider("Sunlight Hours", 0, 14, 10)
pop = st.sidebar.slider("Target Population", 100, 10000, 2500)
diesel = st.sidebar.number_input("Diesel Price ($/Liter)", value=1.20)

# Initialize Agent
agent = SolarWaterAgent(temp, sun, pop, diesel)
results = agent.calculate_metrics()

st.write("---")
m1, m2, m3, m4 = st.columns(4)
m1.metric("⚡ Solar Output", f"{results['solar']:.1f} kWh", delta="Optimal")
m2.metric("💧 Water Demand", f"{results['demand']:.0f} L", delta="Critical", delta_color="inverse")
m3.metric("💰 Daily Savings", f"${results['savings']:.2f}", delta="ROI Positive")
m4.metric("🌿 CO2 Offset", f"{results['carbon']:.1f} kg", delta="Eco-Friendly")

st.write("---")
st.subheader("🤖 AI Strategic Advisor (Llama 3 Insights)")
with st.spinner("Analyzing real-time data..."):
    advice = agent.get_ai_advisor_response(results)
    st.info(advice)

st.write("---")
col_left, col_right = st.columns([1, 1])

with col_left:
    st.write("### 🔋 Supply vs Demand Balance")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie([results['solar'], results['demand']*0.05], 
           labels=['Solar Supply', 'Energy Demand'], 
           autopct='%1.1f%%', 
           colors=['#FAD02C', '#00539C'],
           startangle=90)
    st.pyplot(fig)

with col_right:
    st.write("### 📈 Monthly Financial ROI Projection")
    forecast = pd.DataFrame(
        np.random.randn(30, 1).cumsum() + (results['savings'] * 30),
        columns=['Accumulated Savings ($)']
    )
    st.area_chart(forecast)

st.divider()
st.caption("Developed by Salim Al-Radhwi | Integrating Accounting Principles with AI Engineering")
    

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="BioGuard AI", layout="wide")

st.title("🦣 **BioGuard AI**")
st.markdown("**Wildlife Microbiome Early Warning System**")

# Sidebar: Ranger inputs
st.sidebar.header("Field Sample")
animal_id = st.sidebar.text_input("Animal ID", "Elephant_003")
date = st.sidebar.date_input("Sample Date")
location = st.sidebar.selectbox("Location", ["Zone A", "Zone B", "Zone C"])

# Mock microbiome metrics (Day 1 - fake data)
shannon = st.sidebar.slider("Shannon Diversity", 0.5, 3.0, 1.8, 0.1)
pathogens = st.sidebar.slider("Pathogen Load %", 0, 50, 12)

if st.button("🚨 ANALYZE SAMPLE", type="primary"):
    # Mock AI processing (Day 1)
    risk_score = 75 if shannon > 1.5 else 45 if shannon > 1.0 else 20
    risk_class = "LOW" if risk_score > 70 else "MEDIUM" if risk_score > 40 else "HIGH"
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Diversity", f"{shannon:.2f}", delta=f"{shannon-1.8:+.1f}")
    with col2:
        st.metric("Pathogens", f"{pathogens}%", delta=f"{pathogens-10:+.0f}")
    with col3:
        st.error(f"**RISK: {risk_class}**")
    
    # Population risk heatmap
    pop_data = pd.DataFrame({
        'Zone': ['A', 'B', 'C', 'D'],
        'Risk_Score': [82, 65, 38, 22]
    })
    fig = px.bar(pop_data, x='Zone', y='Risk_Score', 
                 title="Population Risk Heatmap",
                 color='Risk_Score', color_continuous_scale='RdYlGn_r')
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("**Action:** Flag Elephant_003 for veterinary check")

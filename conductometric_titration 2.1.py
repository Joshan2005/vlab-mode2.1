import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Conductometric Titration Simulator", layout="centered")

st.title("🔬 Conductometric Titration Simulator")

# Theory and Aim
with st.expander("📘 AIM, PRINCIPLE & PROCEDURE"):
    st.markdown("""
    **Aim**  
    To find out the strength of hydrochloric acid and acetic acid in a given mixture by titrating it against sodium hydroxide solution, conductometrically.

    **Apparatus**  
    Conductivity meter, burette, pipette, beakers, volumetric flask, etc.

    **Principle**  
    Current is conducted in an electrolytic solution by the movement of positive and negative ions. During titration:
    - For strong acid (HCl), conductance decreases until the equivalence point and then increases.
    - For weak acid (CH₃COOH), conductance increases gradually and then sharply post equivalence.
    
    **Procedure Summary**  
    1. Standardize NaOH using oxalic acid.  
    2. Titrate 10 ml of sample with 0.1 N NaOH in 0.2 ml steps.  
    3. Measure and record conductance after each addition.  
    4. Plot conductance vs. volume added.
    """)

# Input Experimental Data
st.subheader("📊 Enter Conductometric Titration Data")
sample_volume = st.number_input("Volume of sample taken (ml)", value=10.0, step=0.1)
naoh_normality = st.number_input("Normality of NaOH (N)", value=0.1, step=0.01)

data_input = st.text_area("Paste volume (ml) and conductance (mS) values (comma-separated):", 
"""0.0, 4.2
0.2, 4.4
0.4, 4.6
0.6, 4.8
0.8, 5.0
1.0, 5.2
1.2, 5.4
1.4, 5.6
1.6, 5.8
1.8, 6.0
2.0, 6.2
2.2, 6.4
2.4, 6.6
2.6, 6.8
2.8, 7.0
3.0, 7.2
3.2, 7.4
3.4, 7.6
3.6, 7.8
3.8, 8.0
4.0, 8.2""")

# Parse input data
data = []
for line in data_input.strip().split('\n'):
    try:
        vol, cond = map(float, line.strip().split(','))
        data.append((vol, cond))
    except:
        continue

if data:
    df = pd.DataFrame(data, columns=["Volume of NaOH (ml)", "Conductance (mS)"])
    st.dataframe(df)

    # Plotting
    st.subheader("📈 Conductance vs Volume of NaOH Added")
    fig, ax = plt.subplots()
    ax.plot(df["Volume of NaOH (ml)"], df["Conductance (mS)"], marker='o', color='blue')
    ax.set_title("Conductance vs Volume of NaOH Added")
    ax.set_xlabel("Volume of NaOH (ml)")
    ax.set_ylabel("Conductance (mS)")
    ax.grid(True)
    st.pyplot(fig)

# Calculation Section
st.subheader("🧮 Calculations")

vol_HCl = st.number_input("Volume of NaOH consumed for HCl (Vₐ) in mL", value=2.0)
vol_total = st.number_input("Total volume of NaOH consumed (Vb) in mL (HCl + CH₃COOH)", value=5.0)

# Normality of HCl
N_HCl = (naoh_normality * vol_HCl) / sample_volume
mass_HCl = (N_HCl * 36.5 * 100) / 1000  # 36.5 is molar mass

# Normality and Mass of CH₃COOH
vol_CH3COOH = vol_total - vol_HCl
N_CH3COOH = (naoh_normality * vol_CH3COOH) / sample_volume
mass_CH3COOH = (N_CH3COOH * 60 * 100) / 1000  # 60 is molar mass

st.write(f"**Normality of HCl (N₂):** {N_HCl:.3f} N")
st.write(f"**Amount of HCl in whole solution:** {mass_HCl:.3f} g")

st.write(f"**Normality of CH₃COOH (N₃):** {N_CH3COOH:.3f} N")
st.write(f"**Amount of CH₃COOH in whole solution:** {mass_CH3COOH:.3f} g")

# Results
st.subheader("✅ Result")
st.success(f"The amount of HCl in the mixture is **{mass_HCl:.3f} g**")
st.success(f"The amount of CH₃COOH in the mixture is **{mass_CH3COOH:.3f} g**")

# Footer
st.info("You can change experimental values above to see updated calculations and graphs.")

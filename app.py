import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- Header & Identification ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.markdown(f"**Name:** Muhammad Junaid Ali")
st.markdown(f"**Roll Number:** 25-ME-63")
st.divider()

# --- Sidebar Navigation ---
option = st.sidebar.selectbox("Select Functionality", ["Unit Converter", "Material Density Checker"])

# --- Unit Converter Logic ---
if option == "Unit Converter":
    st.header("⚙️ Unit Converter")
    
    category = st.selectbox("Select Category", ["Length", "Pressure", "Energy"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Meters", "Millimeters", "Inches", "Feet"])
        
        # Conversion to Meters first
        to_meters = {"Meters": 1, "Millimeters": 0.001, "Inches": 0.0254, "Feet": 0.3048}
        meters_val = val * to_meters[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Meters", "Millimeters", "Inches", "Feet"])
            result = meters_val / to_meters[unit_to]
            st.metric("Converted Value", f"{result:.4f} {unit_to}")

    elif category == "Pressure":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Pascal (Pa)", "Bar", "PSI"])
            
        to_pa = {"Pascal (Pa)": 1, "Bar": 100000, "PSI": 6894.76}
        pa_val = val * to_pa[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Pascal (Pa)", "Bar", "PSI"])
            result = pa_val / to_pa[unit_to]
            st.metric("Converted Value", f"{result:.4f} {unit_to}")

    elif category == "Energy":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Joules", "Calories", "BTU"])
            
        to_j = {"Joules": 1, "Calories": 4.184, "BTU": 1055.06}
        j_val = val * to_j[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Joules", "Calories", "BTU"])
            result = j_val / to_j[unit_to]
            st.metric("Converted Value", f"{result:.4f} {unit_to}")

# --- Density Checker Logic ---
else:
    st.header("🧪 Material Density Checker")
    st.write("Find the density of common engineering materials.")
    
    densities = {
        "Steel": 7850,
        "Aluminum": 2710,
        "Copper": 8960,
        "Titanium": 4506,
        "Cast Iron": 7200,
        "Water": 1000,
        "Concrete": 2400
    }
    
    material = st.selectbox("Select Material", list(densities.keys()))
    density = densities[material]
    
    st.info(f"The density of **{material}** is approximately **{density} kg/m³**.")
    
    # Simple Mass Calculator
    st.subheader("Mass Calculator")
    vol = st.number_input("Enter Volume (m³)", value=1.0, min_value=0.0)
    mass = vol * density
    st.success(f"Total Mass: {mass:.2f} kg")

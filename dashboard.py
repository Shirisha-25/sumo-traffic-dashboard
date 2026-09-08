import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

st.title("My Traffic Simulation Dashboard")

st.write("This dashboard shows data from my SUMO traffic simulation (mynetwork).")

# Try to load trip data from the SUMO route file
try:
    tree = ET.parse("mynetwork.rou.xml")
    root = tree.getroot()
    trip_data = []
    for vehicle in root.findall("vehicle"):
        trip_data.append({
            "id": vehicle.get("id"),
            "depart": float(vehicle.get("depart"))
        })
    df = pd.DataFrame(trip_data)
    st.write("First 5 trips:")
    st.write(df.head())

    st.subheader("Vehicle Departures Over Time")
    fig, ax = plt.subplots()
    ax.hist(df["depart"], bins=20, color="skyblue")
    ax.set_xlabel("Departure Time (s)")
    ax.set_ylabel("Number of Vehicles")
    st.pyplot(fig)

except Exception as e:
    st.error(f"Could not load data: {e}")
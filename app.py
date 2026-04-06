import streamlit as st
import pandas as pd

# Simulated API response
api_response = {
    "train_name": "Rajdhani Express",
    "train_number": "12301",
    "route": [
        {"station": "New Delhi", "arrival": "Source", "departure": "07:05"},
        {"station": "Kanpur Central", "arrival": "10:10", "departure": "10:15"},
        {"station": "Allahabad Jn", "arrival": "12:00", "departure": "12:10"},
        {"station": "Patna Jn", "arrival": "16:30", "departure": "16:40"},
        {"station": "Howrah Jn", "arrival": "21:30", "departure": "Destination"}
    ]
}

# Convert route data into a DataFrame
route_data = []

for stop in api_response["route"]:
    route_data.append({
        "Station": stop["station"],
        "Arrival": stop["arrival"],
        "Departure": stop["departure"]
    })

train_df = pd.DataFrame(route_data)

# Display train details
st.markdown(f"# {api_response['train_name']}")
st.markdown(f"### Train Number: {api_response['train_number']}")

# Show route table
st.markdown("## Train Route")
st.dataframe(train_df, use_container_width=True)

# Station dropdown
selected_station = st.selectbox(
    "Select a Station",
    train_df["Station"]
)

# Show selected station timings
selected_row = train_df[train_df["Station"] == selected_station].iloc[0]

st.text(f"Arrival Time: {selected_row['Arrival']}")
st.text(f"Departure Time: {selected_row['Departure']}")

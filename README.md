# Train Dashboard

A simple Streamlit web app that displays the route of the Rajdhani Express train using simulated API response data.

## Features

- Displays train name and train number
- Shows the complete train route in a table
- Lets the user select a station from a dropdown
- Displays arrival and departure time for the selected station

## Files in this Project

- `app.py` → Main Streamlit application
- `requirements.txt` → Required Python libraries
- `README.md` → Project description and instructions

## API Response Used

```python
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

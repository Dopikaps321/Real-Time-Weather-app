import streamlit as st
import requests

API_KEY = "6a4710ee1364462c863155043250607"  # Your working WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json"

st.set_page_config(page_title="Weather App", layout="centered")
st.title("🌦️ Simple Weather App")

# Input field
city = st.text_input("Enter city name (e.g., Kozhikode or Kozhikode,IN)")

# When user clicks the button
if st.button("Get Weather"):
    if city:
        params = {
            "key": API_KEY,
            "q": city,
            "aqi": "no"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "current" in data:
            st.success(f"✅ Weather for {data['location']['name']}, {data['location']['country']}")
            st.write(f"🌡️ **Temperature**: {data['current']['temp_c']}°C")
            st.write(f"☁️ **Condition**: {data['current']['condition']['text']}")
            st.write(f"💧 **Humidity**: {data['current']['humidity']}%")
            st.write(f"🌬️ **Wind Speed**: {data['current']['wind_kph']} km/h")
        else:
            st.error("❌ City not found or API error.")
            st.write(data)  # Debug output
    else:
        st.warning("⚠️ Please enter a city name.")

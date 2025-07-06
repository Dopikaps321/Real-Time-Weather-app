# 🌤️ Real-Time Weather App

A simple and responsive weather application built with **Python**, **Streamlit**, and the **WeatherAPI.com** to fetch and display real-time weather data based on user input.

## 🖼️ Demo Screenshot

> *(Optional: Add screenshot.png of your app running here)*

## 🔥 Features

- 🌍 Enter any city name to get real-time weather info
- 🌡️ View temperature, humidity, and wind speed
- ☁️ Shows weather condition (e.g., Sunny, Cloudy)
- 🧠 Easy-to-use interface via **Streamlit**

## 🚀 Technologies Used

- Python
- Streamlit
- WeatherAPI (https://www.weatherapi.com/)
- Requests (Python HTTP Library)

## 🔑 Weather API Info

This app uses a free API key from [WeatherAPI.com](https://www.weatherapi.com/) to fetch weather data:

```url
http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=CityName

##🛠️ Installation & Usage
## Clone the repository

git clone https://github.com/Dopikaps321/Real-Time-Weather-app.git
cd Real-Time-Weather-app
##Install dependencies

pip install streamlit requests
## Run the app

streamlit run weather_streamlit.py
## 📂 Project Structure

Real-Time-Weather-app/
│
├── weather_streamlit.py   # Main Streamlit App
├── weather_app.py         # Optional: CLI version (if retained)
├── README.md              # This file

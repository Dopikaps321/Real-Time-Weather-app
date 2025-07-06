import requests

API_KEY = "6a4710ee1364462c863155043250607"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

city = input("Enter city name: ")

params = {
    "key": API_KEY,
    "q": city,
    "aqi": "no"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if "current" in data:
    print(f"\n✅ Weather for {data['location']['name']}, {data['location']['country']}")
    print(f"🌡️ Temperature: {data['current']['temp_c']}°C")
    print(f"☁️ Condition: {data['current']['condition']['text']}")
    print(f"💧 Humidity: {data['current']['humidity']}%")
    print(f"🌬️ Wind Speed: {data['current']['wind_kph']} km/h")
else:
    print("\n❌ City not found or API error.")
    print(data)  # This will help you debug the issue if any


import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\n🌦️ Weather in {city}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")

else:
    print("❌ City not found or API error")

# Note: Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key to run the code successfully.

import urllib.request
import json

def get_weather_description(code):
    """Convert WMO weather code to readable text."""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
    }
    return descriptions.get(code, f"Unknown weather code ({code})")

def get_weather(city_name):
    # First, get coordinates for the city (geocoding)
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    try:
        with urllib.request.urlopen(geo_url, timeout=10) as resp:
            geo_data = json.loads(resp.read().decode("utf-8"))
        
        if not geo_data.get("results"):
            print(f"City '{city_name}' not found. Try adding country code (e.g., Hanoi,VN).")
            return
        
        result = geo_data["results"][0]
        lat = result["latitude"]
        lon = result["longitude"]
        city = result.get("name", city_name)
        country = result.get("country_code", "")

        # Now get current weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code&timezone=auto"
        with urllib.request.urlopen(weather_url, timeout=10) as resp:
            weather_data = json.loads(resp.read().decode("utf-8"))
        
        current = weather_data["current"]
        temp = current["temperature_2m"]
        code = current["weather_code"]
        description = get_weather_description(code)

        print(f"Location: {city}, {country}")
        print(f"Weather condition: {description}")
        print(f"Temperature: {temp} °C")

    except Exception as e:
        print("Error fetching weather data. Check your internet connection or city name.")

if __name__ == "__main__":
    city = input("Enter the name of the municipality: ").strip()
    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")
        # i dont think it will be long like these
import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"   # Returns temp in Celsius + other metric units
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Extract required fields
        description = data["weather"][0]["description"]
        temp_celsius = data["main"]["temp"]

        print(f"Weather condition: {description}")
        print(f"Temperature: {temp_celsius} °C")

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"City '{city_name}' not found. Please check the spelling or try adding country code (e.g., Hanoi,VN).")
        else:
            print("Error fetching weather data.")
    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
    except (KeyError, IndexError):
        print("Unexpected data format from API.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"  # ← Replace with your OpenWeatherMap API key
    city = input("Enter the name of the municipality: ").strip()
    if city:
        get_weather(city, api_key)
    else:
        print("Please enter a valid city name.")
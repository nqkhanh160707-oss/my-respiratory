import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        data = response.json()
        joke_text = data.get("value")
        if joke_text:
            print(joke_text)
        else:
            print("Sorry, could not retrieve a joke at this time.")
    except requests.exceptions.RequestException as e:
        print("Error fetching joke. Please check your internet connection.")
        # In production, you might log the error: print(f"Debug: {e}")

if __name__ == "__main__":
    get_chuck_norris_joke()
    #i dont have PIP installed but i think you can run it
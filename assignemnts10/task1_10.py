import urllib.request
import json

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print("Error fetching joke. Please check your internet connection.")
    except urllib.error.URLError as e:
        print("Network error. Please check your internet connection.")
    except json.JSONDecodeError:
        print("Error decoding joke data.")
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
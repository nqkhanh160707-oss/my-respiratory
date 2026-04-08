import urllib.request
import json

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            joke_text = data.get("value")
            if joke_text:
                print(joke_text)
            else:
                print("Could not retrieve a joke.")
    except Exception:
        print("Error fetching joke. Check your internet connection.")

if __name__ == "__main__":
    get_chuck_norris_joke()
    #i dont have PIP installed but i think you can run it
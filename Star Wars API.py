import requests
def fetch_data(option):
    url = f"https://swapi.mimo.dev/api/{option}/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Number of entities: {len(data)}")
        return data

    except requests.HTTPError as e:
        print(f"Error: {e}")
        return None

option = input("Enter what StarWars data do you like to explore? ").strip().lower() #people
data = fetch_data(option)

if data:
    for key in data:
        print(key["name"])
    else:
        print("Unable to download data")
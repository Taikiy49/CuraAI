import requests

def location_summary(place_name, state, city):
    API_KEY = 'AIzaSyCpspy8Iw3hPb7TVteMrLAs0X8y7OA5Ca0'
    query = f"{place_name} in {city}, {state}"
    api_url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}'

    response = requests.get(api_url)
    data = response.json()
    place = data['results'][0]
    name = place['name']
    address = place['formatted_address']
    location = place['geometry']['location']

    return [name, address, location['lat'], location['lng']]
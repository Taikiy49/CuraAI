import requests

API_KEY = 'AIzaSyCpspy8Iw3hPb7TVteMrLAs0X8y7OA5Ca0'
location_name = 'New York City'  

# Construct the API request URL
api_url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={location_name}&inputtype=textquery&fields=geometry,formatted_address,name&key={API_KEY}'

# Make the API request
response = requests.get(api_url)
data = response.json()

print(data)
# Process the response
if data['status'] == 'OK' and 'candidates' in data and len(data['candidates']) > 0:
    # Extract relevant information
    place = data['candidates'][0]
    name = place['name']
    address = place['formatted_address']
    location = place['geometry']['location']

    # Do something with the retrieved information
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Latitude: {location['lat']}")
    print(f"Longitude: {location['lng']}")
else:
    print("No results found")

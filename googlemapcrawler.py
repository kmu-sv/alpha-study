import googlemaps
import json
import requests

API_KEY = 'AIzaSyDFtKtm0jnjckE-lB0LkO3SKlWmQIJush8';
gmaps = googlemaps.Client(key=API_KEY)

gmaps_result = gmaps.places_radar(location=(37.778159, -122.411867), radius=500,
                                  min_price=0, max_price=2, open_now=False, type='cafe')

# make list 
data = list()

# gmaps_result has 'results' tag
for place in gmaps_result['results'][0:20]:
    # find place_idd
    place_id = place['place_id']

    # then find json data from place_id
    req_query = 'https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}'.format(place_id, API_KEY)

    # request result recieve and change json
    req = requests.get(req_query).json()
    jsonData = json.dumps(req['result'], indent=4)
    print(jsonData)

    data.append(req['result']['name'])

print(data)

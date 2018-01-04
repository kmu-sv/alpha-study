from flask import Flask
from flask import render_template

import json
import googlemaps

app = Flask(__name__)

@app.route('/')
def hello_world(data=None):
	gmaps = googlemaps.Client(key='AIzaSyBVmmNbiUWw6JQhe9XfsEgrmyAQ6XeW0tM')

	geocode_result = gmaps.places(
		['restaurant', 'cafe'],
		location=(37.7779056, -122.414231),
		radius=300,
		language='en-AU',
		min_price=1,
		max_price=4,
		# open_now=True,
		type='cafe'
		)

	jsonData = json.dumps(geocode_result['results'], indent=4)

	return render_template('index.html', data=geocode_result['results'])
	# # print(jsonData)

	# for place in geocode_result['results']:
	# 	print('%s \t\t lat:%f \t lng:%f' %(place['name'], place['geometry']['location']['lat'], place['geometry']['location']['lng']))


if __name__ == '__main__':
    app.run()
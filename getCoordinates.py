import googlemaps
#from motionless import CenterMap

from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCnVeLt_qHh4zguJBK5zYF85iJvRTCi0eM')
address1 = "246 McAllister St"
city1 = "Takoma Park"
state1 = "MD"

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
def getGeoLocation(address, city, state):
    geocode_result = gmaps.geocode(("%s,%s")%(city, state))
#   geocode_result = gmaps.geocode('Block 9600 14th Bay Street, Norfolk, VA')
    lat = (geocode_result[0]["geometry"]["bounds"]["northeast"]["lat"])
    lng = (geocode_result[0]["geometry"]["bounds"]["northeast"]["lng"])

    return (lat, lng)
#for key in geocode_result[0].items():
#	print (key) 
#print (geocode_result[0].keys())

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
#print (type(directions_result))
#print ((directions_result[0]))
#cmap = CenterMap(address='9600 14th Bay Street, Norfolk, VA')
#print (cmap.generate_url())
location = getGeoLocation(address1, city1, state1)
query = gmaps.places_nearby(location = location, radius = 100)

for place in query["results"]:
	print (place["name"])
	#place_info = (gmaps.place(place_id=place["place_id"]))
	#print (place["name"], place_info["result"]["formatted_address"])
	#if place["name"] == "Black Crow Mine":
	#	place_info = (gmaps.place(place_id=place["place_id"]))
	#	print (place_info["result"]["formatted_address"])
		#print (place["place_id"])
#	print (place["place_id"], place["name"])

#if place["name"] is "Richmond":
#		print (place["long_name"])

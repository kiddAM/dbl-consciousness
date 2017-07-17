import json

import googlemaps
from sqlalchemy import and_

gmaps = googlemaps.Client(key='AIzaSyCnVeLt_qHh4zguJBK5zYF85iJvRTCi0eM')

def getGeoLocation(address, city, state):
    geocode_result = gmaps.geocode(("%s,%s,%s")%(address,city,state))
#   geocode_result = gmaps.geocode('Block 9600 14th Bay Street, Norfolk, VA')
    lat = (geocode_result[0]["geometry"]["bounds"]["northeast"]["lat"])
    lng = (geocode_result[0]["geometry"]["bounds"]["northeast"]["lng"])

    return (lat, lng)

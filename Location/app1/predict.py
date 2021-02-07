import requests
from time import sleep
from .models import Address

for address in Address:
    # Wait a few seconds between each of these because we'd like to pretend
    # we aren't robots and are polite
    sleep(1)
    # Wrap this in try/except because hey if it fails it fails
    try:
        # Form the URL with the address in it
        url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={}".format(address.full_address())

        # Request the URL
        response = requests.get(url)

        # Dig deep into the JSON
        # this will give us something like
        # {u'lat': 40.7135296, u'lng': -73.9856844}
        coords = response.json()['results'][0]['geometry']['location']

        # Assign the lat/lng into the school object (the row)
        address.latitude = coords['lat']
        address.longitude = coords['lng']

        # And now save it to the database
        address.save()

    except None:
        print("error occurred")

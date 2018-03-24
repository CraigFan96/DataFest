import requests
import json

if __name__ == "__main__":
	raw_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
	city = "Boston"
	key = "AIzaSyBM0iUUUOMw1QONaT3w5XntSjT6N_9SMhs"

	r = requests.get(raw_url + city + "&" + key)
	lat_lng = r.json()["results"][0]["geometry"]["location"]
	lat = lat_lng["lat"]
	lng = lat_lng["lng"]

	print(lat, lng)
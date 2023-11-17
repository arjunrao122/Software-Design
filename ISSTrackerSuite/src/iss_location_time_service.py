import requests
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
import time


def get_time_location_response():
    try:
        return requests.get("http://api.open-notify.org/iss-now.json").json()
    except requests.RequestException as e:
        print(f"Error fetching ISS data: {e}")
        return None


def parse_time_location_response(data):
    if data:
        return [data['iss_position']['latitude'], data['iss_position']['longitude'], data['timestamp']]
    return [None, None, None]


def get_location_time():
    location_time = parse_time_location_response(get_time_location_response())
    if None in location_time:
        return "Error: ISS data not available"

    location_time[2] = (datetime.fromtimestamp(location_time[2], pytz.timezone('US/Central'))).strftime("%I:%M %p")

    try:
        geolocator = Nominatim(user_agent="YourAppName_or_YourEmail")
        location = geolocator.reverse(f"{location_time[0]},{location_time[1]}")

        if location is not None:
            city = location.raw['address'].get('city', "City N/A")
            state = location.raw['address'].get('state', "State N/A")
            location_time[0], location_time[1] = city, state
        else:
            location_time[0], location_time[1] = "City N/A", "State N/A"

        return location_time

    except Exception as e:
        print(f"Error in geocoding: {e}")
        return ["City N/A", "State N/A", location_time[2]]

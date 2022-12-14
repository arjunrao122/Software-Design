import requests
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz


def get_time_location_response():
    return requests.get("http://api.open-notify.org/iss-now.json").json()


def parse_time_location_response(data):
    return [data['iss_position']['latitude'], data['iss_position']['longitude'], data['timestamp']]


def get_location_time():
    location_time = parse_time_location_response(get_time_location_response())
    location_time[2] = (datetime.fromtimestamp(location_time[2], pytz.timezone('US/Central'))).strftime("%I:%M %p")
    try:
        location = (Nominatim(user_agent="geoapiExercises")).reverse(location_time[0] + "," + location_time[1])
        location_time[0], location_time[1] = (location.raw['address']).get('city'), (location.raw['address']).get('state')
        if location_time[0] is None:
            location_time[0] = "City N/A"
            return location_time
        else:
            return location_time
    except AttributeError:
        location_time[0], location_time[1] = "City N/A", "State N/A"
        return location_time

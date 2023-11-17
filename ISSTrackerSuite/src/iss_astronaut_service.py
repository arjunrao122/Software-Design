import requests


def get_response():
    return requests.get("http://api.open-notify.org/astros.json").json()


def parse_response(data):
    return [people['name'] for people in data['people'] if people['craft'] == 'ISS']


def get_astronauts_names():
    return parse_response(get_response())

from src.iss_information import *       # pragma: no cover
from src.iss_astronaut_service import get_astronauts_names      # pragma: no cover
from src.iss_location_time_service import get_location_time     # pragma: no cover


def main():     # pragma: no cover
    location_time_list = get_location(get_location_time)
    print('ISS location as', location_time_list[2], 'CT flying over', location_time_list[0], ',', location_time_list[1])
    astronaut_names = get_astronauts(get_astronauts_names)
    print('There are', len(astronaut_names), 'people on ISS at this time:')
    for names in astronaut_names:
        print(names)

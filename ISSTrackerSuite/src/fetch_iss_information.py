from src.iss_information import get_location, get_astronauts
from src.iss_astronaut_service import get_astronauts_names
from src.iss_location_time_service import get_location_time


def print_iss_information(location_time, astronaut_names):
    print('ISS location as of', location_time[2], 'CT flying over', location_time[0], ',', location_time[1])
    print('There are', len(astronaut_names), 'people on ISS at this time:')
    for name in astronaut_names:
        print(name)


def fetch_and_display_iss_information():
    try:
        location_time = get_location(get_location_time)
        astronaut_names = get_astronauts(get_astronauts_names)
        print_iss_information(location_time, astronaut_names)
    except Exception as e:
        print(f"Error fetching ISS information: {e}")


if __name__ == "__main__":
    fetch_and_display_iss_information()

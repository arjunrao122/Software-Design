def get_location(iss_location_service):
    try:
        return iss_location_service()
    except Exception as exception:
        return str(exception)


def get_astronauts(iss_astro_service):
    try:
        return sorted(iss_astro_service(), key=lambda name: name.split(" ")[-1])
    except Exception as exception:
        return str(exception)

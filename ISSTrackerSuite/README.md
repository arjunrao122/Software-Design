# ISS Information Fetching Project

## Overview
This project is designed to fetch and display real-time information about the International Space Station (ISS). It includes functionalities for retrieving the current location and time of the ISS and listing the astronauts currently aboard.

## Features
- Fetching real-time ISS location and time data.
- Listing the names of astronauts currently aboard the ISS.
- Handling errors and exceptions gracefully.

## Modules
- iss_astronaut_service.py: Handles fetching astronaut data from an API.
- iss_information.py: Processes the ISS location and astronaut data.
- iss_location_time_service.py: Retrieves the ISS's current location and time.
- fetch_iss_information.py: Integrates other modules to fetch and display ISS information.

## Requirements
- Python 3.x
- requests library
- pytz library
- geopy library

## Installation
To run this project, first clone the repository:

```bash
git clone [https://github.com/arjunrao122/Software-Design]
cd ISSTrackerSuite
```

## Usage
The script fetch_iss_information.py is the main entry point of the application. When executed, it will:

- Fetch the current location and time of the ISS.
- List the names of the astronauts currently aboard the ISS.
- Display this information in the console.

## Testing
The project includes unit tests for each module:

- test_iss_astronaut_service.py
- test_iss_information.py
- test_iss_location_time_service.py

## Contributing

Contributions to this project are welcome. Please ensure that any pull requests include corresponding unit tests and adhere to the existing code structure.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Arjun Rao - rao.arjun122@gmail.com
Project Link: [https://github.com/arjunrao122/Software-Design]

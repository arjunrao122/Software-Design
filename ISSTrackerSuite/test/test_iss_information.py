import unittest
from src.iss_information import *


class IssInformationTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_get_location_returns_time_and_location_returned_by_service(self):
        iss_service = lambda: ("10:30PM CT", "Houston, TX")

        self.assertEqual(("10:30PM CT", "Houston, TX"), get_location(iss_service))

    def test_get_location_returns_network_error_exception(self):
        iss_service = lambda: exec('raise(Exception("network error: service unreachable"))')

        self.assertEqual("network error: service unreachable", get_location(iss_service))

    def test_get_location_returns_service_failed_exception(self):
        iss_service = lambda: exec('raise(Exception("service failed to respond"))')

        self.assertEqual("service failed to respond", get_location(iss_service))

    def test_get_astronauts_returns_empty_list(self):
        iss_astro_service = lambda: []

        self.assertEqual([], get_astronauts(iss_astro_service))

    def test_get_astronauts_returns_one_name(self):
        iss_astro_service = lambda: ["Jimmy"]

        self.assertEqual(["Jimmy"], get_astronauts(iss_astro_service))

    def test_get_astronauts_two_sorted_names(self):
        iss_astro_service = lambda: ["Niko Bellic", "Jimmy Pegarino"]

        self.assertEqual(["Niko Bellic", "Jimmy Pegarino"], get_astronauts(iss_astro_service))

    def test_get_astronauts_two_unsorted_names(self):
        iss_astro_service = lambda: ["Jimmy Pegarino", "Niko Bellic"]

        self.assertEqual(["Niko Bellic", "Jimmy Pegarino"], get_astronauts(iss_astro_service))

    def test_get_astronauts_returns_network_error_exception(self):
        iss_astro_service = lambda: exec('raise(Exception("network error: service unreachable"))')

        self.assertEqual("network error: service unreachable", get_astronauts(iss_astro_service))

    def test_get_astronauts_returns_service_failed_exception(self):
        iss_astro_service = lambda: exec('raise(Exception("service failed to respond"))')

        self.assertEqual("service failed to respond", get_astronauts(iss_astro_service))


if __name__ == '__main__':
    unittest.main()

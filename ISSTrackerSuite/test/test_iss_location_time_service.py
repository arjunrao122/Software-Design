import unittest
from src.iss_location_time_service import *
import requests
from unittest.mock import patch


class IssLocationTimeTests(unittest.TestCase):

    def test_time_location_response_returns_response_from_webservice(self):
        self.assertEqual("success", get_time_location_response()['message'])

    def test_parse_time_location_response(self):
        input_data = {"message": "success", "iss_position": {"latitude": "-50.1044", "longitude": "34.1283"}, "timestamp": 1665437059}
        output_data = ['-50.1044', '34.1283', 1665437059]

        self.assertEqual(output_data, parse_time_location_response(input_data))

    def test_parse_time_location_another_response(self):
        input_data = {"message": "success", "iss_position": {"latitude": "22.1044", "longitude": "-4.1283"}, "timestamp": 2586471444}
        output_data = ['22.1044', '-4.1283', 2586471444]

        self.assertEqual(output_data, parse_time_location_response(input_data))

    @patch('src.iss_location_time_service.parse_time_location_response')
    def test_get_location_calls_get_time_location_response_and_parse_time_location_response(self, mock_parse_time_location_response):
        mock_parse_time_location_response.return_value = ['-2.4093', '-166.2190', 1665594568]

        self.assertEqual(['City N/A', 'State N/A', '12:09 PM'], get_location_time())

    @patch('src.iss_location_time_service.parse_time_location_response')
    def test_get_location_returns_time_in_current_time(self, mock_parse_time_location_response):
        mock_parse_time_location_response.return_value = ['6.5913', '-159.8117', 1665594746]

        self.assertEqual(['City N/A', 'State N/A', '12:12 PM'], get_location_time())

    @patch('src.iss_location_time_service.parse_time_location_response')
    def test_get_location_returns_city_and_state(self, mock_parse_time_location_response):
        mock_parse_time_location_response.return_value = ['47.6062', '-122.3321', 1665594746]

        self.assertEqual(['Seattle', 'Washington', '12:12 PM'], get_location_time())

    @patch('src.iss_location_time_service.parse_time_location_response')
    def test_get_location_returns_only_state(self, mock_parse_time_location_response):
        mock_parse_time_location_response.return_value = ['49.4231', '-58.9754', 1665596228]

        self.assertEqual(['City N/A', 'Newfoundland and Labrador', '12:37 PM'], get_location_time())

    @patch('src.iss_location_time_service.get_time_location_response')
    def test_get_location_throws_an_exception_if_service_is_unreachable(self, mock_get_response):
        mock_get_response.side_effect = Exception("service unreachable")

        self.assertRaisesRegex(Exception, 'service unreachable', get_location_time)

    @patch('src.iss_location_time_service.get_time_location_response')
    def test_get_location_throws_an_exception_if_service_returns_an_access_error(self, mock_get_response):
        mock_get_response.side_effect = Exception("error getting data")

        self.assertRaisesRegex(Exception, 'error getting data', get_location_time)


if __name__ == '__main__':
    unittest.main()


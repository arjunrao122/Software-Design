import unittest
from src.iss_astronaut_service import *
import requests
from unittest.mock import patch


class IssAstronautServiceResponseTests(unittest.TestCase):

    def test_get_response_returns_response_from_webservice(self):
        self.assertEqual("success", get_response()['message'])

    def test_parse_response(self):
        input_data = {"number": 2, "message": "success", "people": [{"craft": "ISS", "name": "Kjell Lindgren"}, {"craft": "ISS", "name": "Bob Hines"}]}
        output_data = ['Kjell Lindgren', 'Bob Hines']

        self.assertEqual(output_data, parse_response(input_data))

    def test_parse_another_response(self):
        input_data = {"number": 2, "message": "success", "people": [{"name": "Jessica Watkins", "craft": "ISS"}, {"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}]}
        output_data = ['Jessica Watkins']

        self.assertEqual(output_data, parse_response(input_data))

    @patch('src.iss_astronaut_service.parse_response')
    def test_get_astronaut_names_calls_get_response_and_parse_response(self, mock_parse_response):
        mock_parse_response.return_value = ['Kjell Lindgren', 'Bob Hines', 'Samantha Cristoforetti', 'Jessica Watkins']

        self.assertEqual(['Kjell Lindgren', 'Bob Hines', 'Samantha Cristoforetti', 'Jessica Watkins'], get_astronauts_names())

    @patch('src.iss_astronaut_service.get_response')
    def test_get_astronauts_names_throws_an_exception_if_service_is_unreachable(self, mock_get_response):
        mock_get_response.side_effect = Exception("service unreachable")

        self.assertRaisesRegex(Exception, 'service unreachable', get_astronauts_names)

    @patch('src.iss_astronaut_service.get_response')
    def test_get_astronauts_names_throws_an_exception_if_connection_error(self, mock_get_response):
        mock_get_response.side_effect = Exception("error getting data")

        self.assertRaisesRegex(Exception, 'error getting data', get_astronauts_names)


if __name__ == '__main__':
    unittest.main()

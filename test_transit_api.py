import unittest
from app import app

class TestTransitAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_transit_schedule_valid_input(self):
        # Test the endpoint with valid input
        data = {
            "origin_station_id": "123",
            "coordinates": {
                "latitude": "40.712776",
                "longitude": "-74.005974"
            },
            "destination_station_id": "456"
        }
        response = self.app.post('/transit_schedule', json=data)
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on the expected response

    def test_get_transit_schedule_invalid_input(self):
        # Test the endpoint with missing required parameters
        data = {
            "origin_station_id": "123",
            "destination_station_id": "456"
        }
        response = self.app.post('/transit_schedule', json=data)
        self.assertEqual(response.status_code, 400)

    def test_get_transit_schedule_invalid_coordinates(self):
        # Test the endpoint with invalid coordinates
        data = {
            "origin_station_id": "123",
            "coordinates": {
                "latitude": "invalid",
                "longitude": "-74.005974"
            },
            "destination_station_id": "456"
        }
        response = self.app.post('/transit_schedule', json=data)
        self.assertEqual(response.status_code, 400)

    def test_get_transit_schedule_missing_coordinates(self):
        # Test the endpoint with missing coordinates
        data = {
            "origin_station_id": "123",
            "destination_station_id": "456"
        }
        response = self.app.post('/transit_schedule', json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

import json
import requests
import unittest
from app import config

URL_PREFIX = f"http://{config.HOST}:{config.PORT}"


class Tests(unittest.TestCase):

    def test(self):

        with open('fixtures/penny.json', 'r') as f:
            penny = json.load(f)

        r = requests.post(f"{URL_PREFIX}/pets", json=penny)
        self.assertEqual(201, r.status_code, "Couldn't register Penny.")
        j = r.json()
        penny_id = j['id']

        r = requests.get(f"{URL_PREFIX}/pets/{penny_id}")
        self.assertEqual(200, r.status_code, "Penny couldn't be retrieved.")
        j = r.json()
        self.assertEqual(penny['name'], j['name'], "Penny's name is incorrect.")

        r = requests.get(f"{URL_PREFIX}/pets")
        self.assertEqual(200, r.status_code, "Couldn't retrieve pet listing.")
        filtered = [pet for pet in r.json() if pet['id'] == penny_id]
        self.assertEqual(1, len(filtered), "Penny isn't in our pet listing.")

        r = requests.delete(f"{URL_PREFIX}/pets/{penny_id}")
        self.assertEqual(204, r.status_code, "Penny couldn't be deleted.")

        r = requests.get(f"{URL_PREFIX}/pets")
        self.assertEqual(200, r.status_code, "Couldn't retrieve pet listing.")
        filtered = [pet for pet in r.json() if pet['id'] == penny_id]
        self.assertEqual(0, len(filtered), "Penny is still in our pet listing.")


if __name__ == '__main__':
    unittest.main()

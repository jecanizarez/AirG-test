import logging
from http.client import HTTPException
from typing import Dict, List

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("script_1")


class VehicleAPI:
    def __init__(self):
        self._url = "https://swapi.dev/api/vehicles/"
        self._vehicles = []
        self._set_vehicles()

    @staticmethod
    def _make_request(url: str) -> Dict:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()

    def _set_vehicles(self) -> None:
        logger.info("Consulting Vehicle API")
        data = self._make_request(url=self._url)
        while True:
            self._vehicles.extend(data["results"])
            if data["next"]:
                data = self._make_request(url=data["next"])
            else:
                break

    def get_vehicles(self) -> List:
        return self._vehicles


def get_unique_manufacturers(limit: int = 5):
    try:
        api = VehicleAPI()
        logger.info(f"Calculating {limit} unique manufacturers")
        manufacturers = {}
        for vehicle in api.get_vehicles():
            manufacturer = vehicle["manufacturer"].lower()
            if manufacturer not in manufacturers:
                manufacturers[manufacturer] = 1
            else:
                manufacturers[manufacturer] += 1
        unique_manufacturers = []
        for manufacturer, count in manufacturers.items():
            if count == 1:
                unique_manufacturers.append(manufacturer)
            if len(unique_manufacturers) == limit:
                break
        logger.info(f"Unique Manufacturers: \n" + " \n".join(unique_manufacturers))
    except HTTPException:
        print("An error occur while consulting, please try again")
        exit()


if __name__ == "__main__":
    get_unique_manufacturers()

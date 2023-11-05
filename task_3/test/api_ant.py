import json
import requests
from jsonschema.validators import validate


class StoreOrder:
    def __init__(self, url):
        self.url = url

    POST_STORE_ORDER = '/v2/store/order'
    HEADERS_POST = {
        'Content-Type': 'application/json'
    }
    PAYLOAD_POST = json.dumps({
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2023-10-31T15:50:24.545Z",
        "status": "placed",
        "complete": True
    })

    GET_BY_ID = '/v2/store/order/5'
    HEADERS_GET_BY_ID = {}
    PAYLOAD_GET_BY_ID = {}

    DELETE_ID = '/v2/store/order/5'
    HEADERS_DELETE_ID = {}
    PAYLOAD_DELETE_ID = {}

    GET_INVENTORY = '/v2/store/inventory'
    HEADERS_INVENTORY = {}
    PAYLOAD_INVENTORY = {}

    def store_order(self):
        return requests.post(f"{self.url}{self.POST_STORE_ORDER}", headers=self.HEADERS_POST, data=self.PAYLOAD_POST)

    def get_by_id(self, schema: dict):
        response = requests.get(f"{self.url}{self.GET_BY_ID}", headers=self.HEADERS_GET_BY_ID,
                                data=self.PAYLOAD_GET_BY_ID)
        validate(instance=response.json(), schema=schema)
        return response

    def delete_id(self):
        return requests.delete(f"{self.url}{self.DELETE_ID}", headers=self.HEADERS_DELETE_ID,
                               data=self.PAYLOAD_DELETE_ID)

    def get_inventory(self):
        return requests.get(f"{self.url}{self.GET_INVENTORY}", headers=self.HEADERS_INVENTORY,
                            data=self.PAYLOAD_INVENTORY)

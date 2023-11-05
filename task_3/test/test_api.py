from task_3.schemas.order_id import valid_schema
from task_3.test.api_ant import StoreOrder

URL = 'https://petstore.swagger.io'


class TestStoreOrder:
    def test_store_order(self):
        response = StoreOrder(URL).store_order()
        assert response.status_code == 200

    def test_get_by_id(self):
        response = StoreOrder(URL).get_by_id(schema=valid_schema)
        assert response.status_code == 200

    def test_delete_id(self):
        response = StoreOrder(URL).delete_id()
        assert response.status_code == 200

    def test_get_inventory(self):
        response = StoreOrder(URL).get_inventory()
        assert response.status_code == 200

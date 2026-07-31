from datetime import datetime

from fastapi.testclient import TestClient

from ..main import app
from ..controllers import orders as controller


client = TestClient(app)


def test_read_all_orders_endpoint(monkeypatch):
    sample_orders = [
        {
            "customer_id": 2,
            "promotion_id": None,
            "order_type": "Delivery",
            "total_amount": 24.99,
            "order_id": 1,
            "tracking_number": "TEST-TRACK-001",
            "order_status": "Pending",
            "order_date": datetime(2026, 7, 31, 12, 0, 0)
        }
    ]

    def mock_read_all(db):
        return sample_orders

    monkeypatch.setattr(
        controller,
        "read_all",
        mock_read_all
    )

    response = client.get("/orders/")

    assert response.status_code == 200

    response_data = response.json()

    assert len(response_data) == 1
    assert response_data[0]["order_id"] == 1
    assert response_data[0]["tracking_number"] == "TEST-TRACK-001"
    assert response_data[0]["order_status"] == "Pending"
    assert response_data[0]["total_amount"] == 24.99
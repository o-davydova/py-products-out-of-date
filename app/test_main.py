import datetime
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.fixture()
def products_template():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 320
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime, products_template):
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products_template) == ['duck']

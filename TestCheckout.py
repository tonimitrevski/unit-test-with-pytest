import pytest
from Checkout import Checkout


@pytest.fixture()
def checkout():
    co = Checkout()
    return co


def test_can_add_item_price(checkout):
    additemPrice = checkout.add_item_price('a', 3)


def test_can_add_item(checkout):
    additemPrice = checkout.add_item('a')

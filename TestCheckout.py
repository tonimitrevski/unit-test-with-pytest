import pytest
from Checkout import Checkout


@pytest.fixture()
def checkout():
    co = Checkout()
    return co


def test_can_add_item_price(checkout):
    checkout.add_item_price('a', 3)


def test_can_add_item(checkout):
    checkout.add_item('a')


def test_can_total(checkout):
    checkout.add_item_price('a', 1)
    checkout.add_item('a')
    assert checkout.calculate_total() == 1

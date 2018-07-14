import pytest
from Checkout import Checkout


@pytest.fixture()
def checkout():
    co = Checkout()
    return co


def test_can_total(checkout):
    checkout.add_item_price('a', 1)
    checkout.add_item('a')
    assert checkout.calculate_total() == 1


def test_get_correct_total_with_multiple_items(checkout):
    checkout.add_item_price('a', 1)
    checkout.add_item_price('b', 2)
    checkout.add_item('a')
    checkout.add_item('b')
    assert checkout.calculate_total() == 3

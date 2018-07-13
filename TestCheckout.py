from Checkout import Checkout


def test_can_instance_checkout():
    co = Checkout()


def test_can_add_item_price():
    co = Checkout()
    additemPrice = co.add_item_price('a', 3)

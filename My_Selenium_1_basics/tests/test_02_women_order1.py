from pages.womens_stuff_page import WomensPage
from pages.womens_stuff_page import DiscountCode
from pages.womens_stuff_page import ShoppingCart

import random
import string
import time
import pytest

def test_women_order(driver):
    womens_stuff_page = WomensPage(driver)
    womens_stuff_page.navigate_to_site1()
    womens_stuff_page.navigate_by_menu_wmn_shorts()
    womens_stuff_page.erika_run_shorts_details()
    time.sleep(5)
def test_discount_code_operation(driver, original_price=None):
    discount_code = DiscountCode(driver)
    discount_code.apply_discount_code()
    # discount_code.get_discount_confirmation_txt()
    # discount_code.verify_discount_applied(original_price)
def test_shopping_cart_and_finish(driver):
    shopping_cart = ShoppingCart(driver)
    shopping_cart.shopping_cart_actions()
    shopping_cart.shipping_actions()


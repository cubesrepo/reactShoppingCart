import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.order(1)
class TestHome(BaseTest):
    def test_checkout_without_product_in_cart(self, driver):
        homepage = HomePage(driver)
        homepage.verify_checkout_without_products_in_cart()
    def test_add_to_cart_all_products_and_checkout(self, driver):
        homepage = HomePage(driver)
        sub_total = homepage.verify_add_to_cart_all_products()
        homepage.verify_checkout_all_products_in_cart(sub_total)
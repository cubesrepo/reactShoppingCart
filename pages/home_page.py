import time

from selenium.webdriver.common.by import By
from selenium.common import ElementClickInterceptedException
import test_data
from pages.base_page import BasePage


class HomePage(BasePage):
    def verify_checkout_without_products_in_cart(self):
        time.sleep(2)

        #click cart
        self.wait_clickable(test_data.home.CART_BTN, 15).click()

        time.sleep(0.5)

        #click checkout
        self.wait_clickable(test_data.home.CHECK_OUT_BTN, 10).click()

        time.sleep(0.5)

        #get the text in alert
        textalert = self.get_alert_text()

        #check assertion of textalert
        assert "Add some product in the cart!" in textalert

        time.sleep(0.5)

        #click ok
        self.alert_accept()

        time.sleep(0.2)

        #click x
        self.wait_clickable(test_data.home.X,15).click()

    def verify_add_to_cart_all_products(self):
        time.sleep(2)

        #check page title
        assert self.title_is("Typescript React Shopping cart")
        self.scroll_by_amount(0, 100)
        # store the product_lists_price
        product_lists = []
        sub_total = ""
        for i in range(1, 17):

            # loop for clicking x when the product is at the 3rd in each row
            if i % 4 == 3 or i % 4 == 0:
                x = self.wait_clickable(test_data.home.X, 15)
                try:
                    x.click()
                except ElementClickInterceptedException:
                    self.action_click(x)
                time.sleep(0.2)

            #addtocart btn xpath
            ADD_TO_CART_BTN = By.XPATH, f"(//button[@class='sc-124al1g-0 jCsgpZ'][normalize-space()='Add to cart'])[{i}]"

            #click addto cart btn
            addto_cart = self.wait_presence(ADD_TO_CART_BTN, 5)
            try:
               self.action_click(addto_cart)
            except ElementClickInterceptedException:
                self.action_click(addto_cart)

            time.sleep(0.2)

            #get the text of badge count
            badge_count = self.get_text(test_data.home.BADGE_COUNT, 15)

            #assertion of badge count is adding
            print(f"badge count  {badge_count}")
            assert i == int(badge_count), "the badge count is not upadting"

            time.sleep(0.2)

            #locators of product price
            product_price_xpath = By.XPATH, f"(//p[contains(text(),'$')])[{i}]"

            #get the text of product
            product_price = self.get_text(product_price_xpath, 10).replace('$ ', '')

            #add the product in lists
            product_lists.append(float(product_price))

            total = 0
            #sum up all in product lists
            for p in product_lists:
                total += p

            #get the text of sub total
            sub_total = self.get_text(test_data.home.SUB_TOTAL, 15).replace('$ ', '')
            print(f"total {total}")
            print(f"subtotal {sub_total}")

            #check if the total is the same as sub total
            assert round(float(total), 1) == round(float(sub_total), 2)

        return sub_total

    def verify_checkout_all_products_in_cart(self, sub_total):
        time.sleep(2)

        #click checkout btn
        self.wait_clickable(test_data.home.CHECK_OUT_BTN, 15).click()

        time.sleep(0.5)

        #get the text alert
        textalert = self.get_alert_text().replace('Checkout - Subtotal: $ ', '')
        print(f"text alert total {textalert}")
        print(f"subtotal {sub_total}")

        #compare the subtotal and subtotal from alert
        assert textalert == sub_total

        time.sleep(0.5)

        #click alert ok
        self.alert_accept()





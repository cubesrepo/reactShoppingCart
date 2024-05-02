from selenium.webdriver.common.by import By

BASE_URL = "https://react-shopping-cart-67954.firebaseapp.com/"

class home:
    X = By.XPATH, "(//button[@class='sc-1h98xa9-0 gFkyvN'])[1]"
    BADGE_COUNT = By.XPATH, "(//div[@class='sc-1h98xa9-3 VLMSP'])[1]"
    SUB_TOTAL = By.XPATH, "(//p[@class='sc-1h98xa9-9 jzywDV'])[1]"
    CHECK_OUT_BTN = By.XPATH, "(//button[normalize-space()='Checkout'])[1]"
    CART_BTN = By.XPATH, "(//div[@class='sc-1h98xa9-2 fGgnoG'])[1]"
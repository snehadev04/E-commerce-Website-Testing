from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestProductSearch(unittest.TestCase):

    def setUp(self):
        # Setting up Chrome WebDriver using WebDriver Manager
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        # Closing the WebDriver instance after each test
        self.driver.quit()

    def test_login_and_add_to_cart(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        try:
            # Wait until the inventory page is loaded
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
            )

            # Adding an item to the cart (let's add the first item)
            add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
            add_to_cart_button.click()

            # Verify that the cart icon shows the count of items added
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert cart_badge.text == "1", "Cart count does not match"

            # Open the cart
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

            # Verify the item in the cart
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
            )

            # Assert that the item in the cart matches the added item
            cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name")
            assert "Sauce Labs Backpack" in cart_item_name.text, "Item in cart does not match"

        except Exception as e:
            # Printing current URL and page source for debugging purposes
            print(f"Current URL: {driver.current_url}")
            print(f"Page Source: {driver.page_source}")
            raise e

if __name__ == "__main__":
    unittest.main()

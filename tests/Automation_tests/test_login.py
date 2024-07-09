from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.quit()

    def test_login_valid(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        self.assertIn("inventory.html", driver.current_url)

    def test_login_invalid(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        self.assertIn("Username and password do not match any user in this service", error_message)

    def test_logout(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Open the menu
        driver.find_element(By.ID, "react-burger-menu-btn").click()

        # Wait until the logout link is clickable
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()

        # Verify that the user is redirected to the login page
        self.assertIn("saucedemo.com", driver.current_url)


if __name__ == "__main__":
    unittest.main()

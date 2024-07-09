from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

try:
    # Login
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # Search for a product and add to cart
    product_name = "Sauce Labs Backpack"
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Proceed to checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Enter checkout information
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Finish checkout
    driver.find_element(By.ID, "finish").click()

    # Verify checkout complete
    checkout_complete_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert "THANK YOU FOR YOUR ORDER" in checkout_complete_element.text.upper()
    print("Order placed successfully!")

    # Click on 'Back Home'
    back_home_button = driver.find_element(By.XPATH, "//button[text()='Back Home']")
    back_home_button.click()

    # Verify navigation to home page
    assert "https://www.saucedemo.com/" in driver.current_url
    print("Navigated back to home page after checkout.")

except Exception as e:
    print(f"Failed: {e}")

finally:
    # Close the browser
    driver.quit()

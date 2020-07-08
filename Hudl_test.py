import unittest

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):
    def test_invalid_password(self):

        browser = Chrome()

        try:
            browser.implicitly_wait(2)

            browser.get('http://www.hudl.com/login')

            # Enter username and incorrect password
            browser.find_element_by_id("email").send_keys("nick@threecandles.co.uk")
            browser.find_element_by_id("password").send_keys("test")
            browser.find_element_by_id("logIn").click()

            # Expect login error text to be shown within 2 seconds
            wait = WebDriverWait(browser, 2)
            wait.until(EC.visibility_of(browser.find_element_by_class_name("login-error-container")),
                       "Login error help not displayed")
        finally:
            browser.close()

    def test_valid_login(self):

        browser = Chrome()

        try:
            browser.implicitly_wait(2)
            browser.get('http://www.hudl.com/login')

            # Enter username and incorrect password
            browser.find_element_by_id("email").send_keys("nick@threecandles.co.uk")
            browser.find_element_by_id("password").send_keys("u4ATErJwg4RJ8h9GBjZoCaQMoqCYJ7O9BSZt2bHELZTAzO6nX5")
            browser.find_element_by_id("logIn").click()

            # Should open the hudl home page
            wait = WebDriverWait(browser, 2)
            wait.until(EC.visibility_of(browser.find_element_by_id("home-content")), "Home Page not displayed")
            assert browser.current_url == "https://www.hudl.com/home"
        finally:
            browser.close()

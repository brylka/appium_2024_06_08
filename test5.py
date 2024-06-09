import datetime
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAplicationTests(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'  # Zmień na nazwę Twojego urządzenia lub emulatora
        options.app_package = 'com.example.myapplication'  # Zaktualizuj nazwę pakietu aplikacji
        options.app_activity = '.MainActivity'  # Zaktualizuj nazwę aktywności, jeśli jest inna
        options.automation_name = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723', options=options)

    def test_greeting(self):
        name = 'Bartosz'
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Input Field'))
        )
        input_field.send_keys(name)
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Input Field'))).send_keys(name)

        greet_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Greet Button'))
        )
        greet_button.click()

        greeting_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Greeting Message'))
        )

        self.assertTrue(greeting_message.is_displayed())
        self.assertIn(name, greeting_message.text)


    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
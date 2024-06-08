import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyAplicationTests(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'  # Zmień na nazwę Twojego urządzenia lub emulatora
        options.app_package = 'com.example.myapplication'  # Zaktualizuj nazwę pakietu aplikacji
        options.app_activity = '.MainActivity'  # Zaktualizuj nazwę aktywności, jeśli jest inna
        options.automation_name = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723', options=options)

    def test_hello_android(self):
        greeting_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[contains(@text, 'Hello Android!')]"))
        )
        self.assertIn('Hello Android!', greeting_text.text)

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()

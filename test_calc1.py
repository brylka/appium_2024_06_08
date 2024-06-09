import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

class MyAplicationTests(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'  # Zmień na nazwę Twojego urządzenia lub emulatora
        options.app_package = 'com.example.myapplication'  # Zaktualizuj nazwę pakietu aplikacji
        options.app_activity = '.MainActivity'  # Zaktualizuj nazwę aktywności, jeśli jest inna
        options.automation_name = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723', options=options)

    def test_2_plus_2(self):
        #button_2 = WebDriverWait(self.driver, 10).until(
        #    EC.presence_of_element_located((By.XPATH, "//*[@content-desc='Przycisk 2']"))
        #)
        #button_2.click()

        button_2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Przycisk 2'))
        )
        button_2.click()

        button_plus = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Przycisk +'))
        )
        button_plus.click()

        button_2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Przycisk 2'))
        )
        button_2.click()

        button_equal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Przycisk ='))
        )
        button_equal.click()

        result_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Wynik:')]"))
        )

        result_correct = 4.0
        result = float(result_text.text.split()[1])
        self.assertEqual(result, result_correct)

        result_correct_str = 'Wynik: 4.0'
        result_str = result_text.text
        self.assertEqual(result_correct_str, result_str)


    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
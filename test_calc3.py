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

    def test_calculator(self):

        for a in range(2,5):
            self.click_button(a)
            self.click_button("+")
            self.click_button(a)
            self.click_button("=")

            result_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Wynik:')]"))
            )

            result_correct = float(a+a)
            result = float(result_text.text.split("Wynik: ")[1])
            self.assertEqual(result, result_correct)

            self.click_button("C")


    def click_button(self, label):
        button = WebDriverWait(self.driver, 10).until(
            #EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Przycisk ' + str(label)))
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"Przycisk {label}"))
        )
        button.click()

        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"Przycisk {label}"))).click()

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
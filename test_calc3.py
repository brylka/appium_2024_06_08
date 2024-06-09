import random
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

        for _ in range(10):
            #a = random.randint(0,999)
            #b = random.randint(0,999)
            c = [1,2,3,4,53,42,4234,234,324,34,534,65345,654,3654,6,4355,34,532,4,256,55,8776,89,6574,654]
            a = random.choice(c)
            b = random.choice(c)
            d = random.choice(["+", "-", "*", "/"])
            #buttons = str(a) + "+" + str(a) + "="
            #buttons = f"{a}+{a}="
            for button in f"{a}{d}{b}=":
                self.click_button(button)
            #for button in str(a):
            #    self.click_button(button)
            #self.click_button("+")
            #for button in str(a):
            #    self.click_button(button)
            #self.click_button("=")

            result_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Wynik:')]"))
            )

            result_correct = None
            if d == "+":
                result_correct = float(a + b)
            elif d == "-":
                result_correct = float(a - b)
            elif d == "*":
                result_correct = float(a * b)
            elif d == "/":
                result_correct = float(a / b)
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
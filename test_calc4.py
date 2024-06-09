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

    def test_0_2_add_2_mul_2(self):
        for button in '2+2*2=':
            self.click_button(button)

        result_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Wynik:')]"))
        )

        result = float(result_text.text.split("Wynik: ")[1])
        result_correct = 6.0
        #self.assertEqual(result, result_correct)

        self.click_button("C")

    def test_1_division_by_0(self):
        for buttons in ["0/0=", "123/0=", "98765/0="]:
            for button in buttons:
                self.click_button(button)

            result_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Wynik:')]"))
            )

            result = result_text.text.split("Wynik: ")[1]
            result_correct = 'Błąd dzielenia przez 0'
            self.assertEqual(result, result_correct)

            self.click_button("C")

    def test_2_other_tests(self):
        for _ in range(10):
            a = random.choice([0,0,0,0,12,213,345,456])
            b = 0
            d = random.choice(["+", "-", "*"])
            for button in f"{a}{d}{b}=":
                self.click_button(button)

            result_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Wynik:')]"))
            )

            if d == "+":
                result_correct = float(a + b)
            elif d == "-":
                result_correct = float(a - b)
            else:
                result_correct = float(a * b)

            result = float(result_text.text.split("Wynik: ")[1])
            self.assertEqual(result, result_correct)

            self.click_button("C")

    def test_3_calculator(self):
        for d in ["+", "-", "*", "/"]:
            for _ in range(0):
                a = random.randint(0,999)
                b = random.randint(1,999)
                for button in f"{a}{d}{b}=":
                    self.click_button(button)

                result_text = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Wynik:')]"))
                )

                if d == "+":
                    result_correct = float(a + b)
                elif d == "-":
                    result_correct = float(a - b)
                elif d == "*":
                    result_correct = float(a * b)
                else:
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
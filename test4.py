import datetime
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

    def test_display_current_date(self):
        expected_date = datetime.date.today().strftime("%Y-%m-%d")

        simple_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@content-desc='Prosty Przycisk']"))
        )
        simple_button.click()

        date_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, '{expected_date}')]"))
        )

        self.assertTrue(simple_button.is_displayed())
        self.assertIn(expected_date, date_text.text)

    def test_display_current_time(self):
        # Pobieranie aktualnego czasu
        expected_time = datetime.datetime.now() - datetime.timedelta(hours=2)

        time_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@content-desc='Przycisk Godziny']"))
        )
        time_button.click()

        # Oczekiwanie na pojawienie się tekstu z godziną
        time_text = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@text, 'Aktualna godzina:')]"))
        )
        self.assertTrue(time_text.is_displayed())

        # Pobranie wyświetlonego czasu z aplikacji
        displayed_time_str = time_text.text.split("Aktualna godzina: ")[1]

        # Konwersja wyświetlonego czasu na obiekt datetime, uwzględniając tylko godzinę, minutę, sekundę
        now = datetime.datetime.now()
        displayed_time = now.replace(hour=int(displayed_time_str.split(":")[0]),
                                     minute=int(displayed_time_str.split(":")[1]),
                                     second=int(displayed_time_str.split(":")[2]))

        # Sprawdzenie, czy czas wyświetlony w aplikacji mieści się w zakresie ±15 sekund od oczekiwanego czasu
        time_difference = abs((displayed_time - expected_time).total_seconds())
        self.assertLessEqual(time_difference, 15)



    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
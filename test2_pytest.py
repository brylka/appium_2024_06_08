import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'emulator-5554'  # Zmień na nazwę Twojego urządzenia lub emulatora
    options.app_package = 'com.example.myapplication'  # Zaktualizuj nazwę pakietu aplikacji
    options.app_activity = '.MainActivity'  # Zaktualizuj nazwę aktywności, jeśli jest inna
    options.automation_name = 'UiAutomator2'

    driver = webdriver.Remote('http://localhost:4723', options=options)
    yield driver
    driver.quit()

def test_simple_button(driver):
    simple_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@content-desc='Prosty Przycisk']"))
    )
    assert simple_button.is_displayed()
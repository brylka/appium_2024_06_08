import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.options.android import UiAutomator2Options

class LoginTest(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = '127.0.0.1:5556'
        options.browser_name = 'Chrome'
        options.chromedriver_executable = '/xxx/chromedriver.exe'
        options.automation_name = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723', options=options)

    def test_login(self):
        self.driver.get('http://vesemir.wiedzmin.net:5000')

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="login"]'))
        )

        self.driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys('test')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys('qwer1234')
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )

        welcome_text = self.driver.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Witaj, test', welcome_text)

        time.sleep(5)

    def tearDown(self):
        if self.driver:
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()

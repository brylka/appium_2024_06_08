import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyAplicationTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_hello_android(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

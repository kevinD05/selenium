import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import ActionChains
import time
from selenium.webdriver.common.by import By

class UsandoUnittest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        driver_path = r'C:\driver\chromedriver.exe'
        os.environ["PATH"] += os.pathsep + driver_path
     
        self.driver = webdriver.Chrome(options=options)
    
    def test_css_selector(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_custom_checkbox.asp')

        content = driver.find_element(By.CSS_SELECTOR, 'a.w3-blue')
        content.click()
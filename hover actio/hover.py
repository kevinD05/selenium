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
    
    def test_hover(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(3)

        elem = driver.find_element(By.LINK_TEXT, 'Privacidad')

        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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
    
    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(3)
          
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get('http://python.org')
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
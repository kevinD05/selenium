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
    

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(5)
        buscar_por_xpath = driver.find_element(By.XPATH, '//*[@name="q"]')
        time.sleep(3)
        buscar_por_xpath.send_keys('selenium', Keys.ARROW_DOWN)
        time.sleep(3)
  

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

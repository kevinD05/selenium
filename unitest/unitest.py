import unittest
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

class UsandoUnittest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        driver_path = r'C:\driver\geckodriver.exe'
        os.environ["PATH"] += os.pathsep + driver_path

        self.driver = webdriver.Firefox(options=options)
    
    def test_buscar(self):
        driver = self.driver
        driver.get('http://www.google.com')
        self.assertIn('Google', driver.title)
        elemento = driver.find_element(By.NAME, 'q')
        elemento.send_keys('selenium')
        elemento.send_keys(Keys.RETURN)
        time.sleep(4)
        assert 'No se encontro el elemento:' not in driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

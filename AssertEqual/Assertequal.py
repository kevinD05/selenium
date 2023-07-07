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

    def test_assertequal(self):
        driver = self.driver
        driver.ger('http://www.google.com')
        titulo =driver.title
        time.sleep(2)
        self.assertEqual('Google', titulo, 'Titulo de la pagina no es igual')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
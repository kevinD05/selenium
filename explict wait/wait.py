import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class UsandoUnittest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        driver_path = r'C:\driver\chromedriver.exe'
        os.environ["PATH"] += os.pathsep + driver_path
     
        self.driver = webdriver.Chrome(options=options)
    
    def test_usando_wait(self):
        driver = self.driver
        driver.get('http://www.google.com')
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
            )
        finally:
            driver.quit()


if __name__  == "__main__":
    unittest.main()
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    
    def test_button (self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_custom_checkbox.asp')

        button = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/input[4]')
        button.click()
        time.sleep(3)

        button2 = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/input[3]')
        button2.click()
        time.sleep(3)

    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
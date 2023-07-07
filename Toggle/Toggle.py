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

    def test_toggle(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_switch.asp')
        time.sleep(3)
        toggle = driver.find_element(By.XPATH, '//*[@id="main"]/label[3]/div')
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
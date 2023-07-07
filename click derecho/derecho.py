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
    
    def test_click_derecho(self):
        self.driver.get('https://demoqa.com/buttons')
        clickderecho = self.driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
        actions = ActionChains(self.driver)
        actions.context_click(clickderecho).perform()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
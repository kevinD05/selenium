import unittest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

    def test_select_for(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')

        select = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/select')
        opcion = select.find_elements(By.TAG_NAME, 'option')
        time.sleep(3)
        for option in opcion:
            print('Los valores son: %s' + option.get_attribute('value'))
            option.click()
            time.sleep(1)
        seleccionar = Select(driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/select'))
        seleccionar.select_by_value('10')
        time.sleep(5)

    
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

        
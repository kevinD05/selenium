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
    
    def test_busqueda(self):
        driver = self.driver
        driver.get('http://www.google.com')
        busqueda = driver.find_element(By.NAME, 'q')
        busqueda.send_keys('selenium')
        busqueda.submit()
        time.sleep(3)

    def test_scroll_down(self):
        driver = self.driver
        driver.get("http://www.amazon.com")
        time.sleep(3)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)

    def test_link_por_texto(self):
        driver = self.driver
        driver.get('https://www.w3schools.com')
        time.sleep(3)
        continue_link = self.driver.find_element(By.LINK_TEXT, 'Learn python')
        continue_link.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestrunner.HTMLTestRunner(output='resultado de mi test plan'))
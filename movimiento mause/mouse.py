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

    def test_mouse(self):
       self.driver.get("https://www.youtube.com/watch?v=44bEWzrQTeM&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=42&ab_channel=NicolasAlvarez")
       time.sleep(2)
       mouse = self.driver.find_element(By.XPATH, "//*[@id=user-indicator]/nav[1]/ul/li[3]/a")
       mouse_2 = self.driver.find_element(By.XPATH, '//*[@id="user-indicator"]/nav[1]/ul/li[2]/a')
       movimiento = ActionChains(self.driver)
       movimiento.move_to_element(mouse).move_to_element(mouse_2).click().perform() 
       time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
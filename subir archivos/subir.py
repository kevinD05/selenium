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

    def test_subir(self):
        self.driver.get('https://demoqa.com/upload-download')
        time.sleep(3)
        self.driver.find_element(By.ID, 'input-file-now-custom-2').send_keys('C:\Users\Kevin\Pictures\Feedback\{4E29E0A2-4D5C-49F3-A7B4-73F294EC0126}')
        time.sleep(3)
       
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
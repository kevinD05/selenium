import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configuración del navegador
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

# Ruta del controlador del navegador
driver_path = r'C:\driver\chromedriver.exe'
os.environ["PATH"] += os.pathsep + driver_path

# Inicializar el navegador
driver = webdriver.Chrome(options=options)

try:
    driver.get('file:///C:/Users/Kevin/OneDrive/Documents/Selenium/promp%20alert/alert.html')
    time.sleep(3)
    alert =driver.find_element(By.NAME, 'prompt_alert')
    alert.click()
    time.sleep(3)
    alert = driver.switch_to_alert()
    alert.dismiss()
    time.sleep(3)
    
finally:
     driver.quit()
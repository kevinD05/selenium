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

driver = webdriver.Chrome(options=options)
driver.get('https://www.w3schools.com/html/default.asp')
time.sleep(3)

all_cookies = driver.get_cookies()

print(all_cookies)
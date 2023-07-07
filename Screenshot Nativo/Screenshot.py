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
driver.get('https://www.youtube.com/watch?v=DnsNYxDbaAA&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=36&ab_channel=NicolasAlvarez')
driver.get_screenshot_as_file('C:\Users\Kevin\OneDrive\Documents\Selenium\Screenshot Nativo')
driver.close()
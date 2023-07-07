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

driver.get('http://www.amazon.com')
time.sleep(3)
driver.execute_script('window.scrollTo(0,document.scrollHeight)')
time.sleep(2)
driver.close()
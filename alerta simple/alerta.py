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

# Realizar la automatización
try:
    # Abrir una página web
    driver.get('file:///C:/Users/Kevin/OneDrive/Documents/Selenium/alerta%20simple/alerta._simple.html')
    time.sleep(5)
    # Encontrar elementos y realizar acciones
    element = driver.find_element(By.NAME, 'alert')
    element.click()
    time.sleep(3)
    element=driver.switch_to_alert()
    element.dismiss()
    time.sleep(3)

finally:
    # Cerrar el navegador
    driver.quit()
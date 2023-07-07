import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

# Establece la variable de entorno PATH con la ubicación del directorio que contiene geckodriver.exe
driver_path = r'C:\driver\geckodriver.exe'
os.environ["PATH"] += os.pathsep + driver_path

# Crea una instancia del controlador de Firefox utilizando las opciones
driver = webdriver.Firefox(options=options)
driver.get('http://gmail.com')


usario = driver.find_element(By.ID, "identifierId")
usario.send_keys('alexanderkevindiaz05@gmail.com')
usario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element(By.NAME, 'Passwd')
clave.send_keys('12345')
clave.send_keys(Keys.ENTER)
time.sleep(3)
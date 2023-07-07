import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

# Establece la variable de entorno PATH con la ubicación del directorio que contiene geckodriver.exe
driver_path = r'C:\driver\geckodriver.exe'
os.environ["PATH"] += os.pathsep + driver_path

# Crea una instancia del controlador de Firefox utilizando las opciones
driver = webdriver.Firefox(options=options)
driver.get('http://python.org')

# Continúa con el resto de tu código...

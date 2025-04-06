# comandos para su uso en el webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import time
import urllib.parse 

#Configuración Navegador

def portal_dimensional():
    opciones = Options()
    opciones.add_argument("--window.size=1100,700")
    opciones.add_argument("--disable-notifications")

    servicio = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=servicio,options=opciones)

navegador = portal_dimensional()
navegador.get("https://www.google.com")
input("Presiona Enter para cerrar el navegador...")
navegador.quit 
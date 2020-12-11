import os
import selenium
from selenium import webdriver
import pyautogui
import time
CD_PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(CD_PATH)
driver.set_window_size(1920-48, 1080)

#Informacion inicio de sesión
email = os.getenv("AMAZON_EMAIL")
pwd = os.getenv("AMAZON_PWD")

#producto a buscar
pipas = 'Pipas G Grefusa - Pipas Tijuana, 165 g'

driver.get("https://amazon.es")

#Entrar en la página de identificacion
driver.find_element_by_id('nav-link-accountList').click()

#Introducir email
driver.find_element_by_id('ap_email').send_keys(email) #Escribir email
driver.find_element_by_id('continue').click() #Continuar
#Introducir contraseña
driver.find_element_by_id('ap_password').send_keys(pwd) #Escribir contraseña
driver.find_element_by_id('signInSubmit').click() #Iniciar sesión

driver.find_element_by_id('twotabsearchtextbox').send_keys(pipas) #Buscar pipas en el buscador
pyautogui.hotkey('enter') #Pulsa enter
time.sleep(4)
#Click en la primera aparicion de pipas
driver.find_elements_by_css_selector(f'[alt="{pipas}"')[0].click()

#Click en la primera aparición de compra única
driver.find_elements_by_xpath("//span[contains(text(), 'Compra única')]")[0].click()

comprar = driver.find_element_by_id('buy-now-button')
driver.execute_script("arguments[0].click();", comprar)

time.sleep(3)
driver.find_elements_by_id('shipToThisAddressButton')[0].click() #Seleccionar direccion
time.sleep(3)
driver.find_elements_by_class_name("apx-compact-continue-action")[0].click() #Seleccionar metodo de pago
time.sleep(3)
driver.find_elements_by_id("bottomSubmitOrderButtonId")[0].click() #Realizar compra

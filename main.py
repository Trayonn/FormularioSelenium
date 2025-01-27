from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = Options()

gecko_driver_path = r"CAMINHO DO GECKODRIVER OU CHROMEDRIVER"  # Substitua pelo caminho correto

service = Service(gecko_driver_path)
driver = webdriver.Firefox(options=options, service=service)

driver.get("http://localhost:8000/index.html")

time.sleep(3)


inserir_nome = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "nome"))
)
inserir_nome.click()

inserir_nome.send_keys("Nome do Usuário")


inserir_email = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "email"))
)
inserir_email.click()

inserir_email.send_keys("teste@gmail.com")


inserir_senha = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "senha"))
)
inserir_senha.click()

inserir_senha.send_keys("senhaexemplo")

confirmar_senha = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "confirmarSenha"))
)
confirmar_senha.click()

confirmar_senha.send_keys("senhaexemplo")

sobre_mim = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "sobreMim"))
)
sobre_mim.click()

sobre_mim.send_keys("Texto de exemplo.")


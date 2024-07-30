import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib

contatos = ['Insira o numero de seus contatos entre aspas e separados por ,']

navegador = webdriver.Chrome()

navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(1)

for contato in contatos:
    mensagem = f'Mensagem enviada via script para {contato}'
    mensagemEncoded = urllib.parse.quote(mensagem)
    link = f'https://web.whatsapp.com/send?phone={contato}&text={mensagemEncoded}'
    
    navegador.get(link)

    while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')) < 1:
        time.sleep(1)
    
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
    time.sleep(10)
    
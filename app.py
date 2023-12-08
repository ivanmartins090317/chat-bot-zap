import time
import urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


chromeExec =  Service(ChromeDriverManager().install())
navegador =webdriver.Chrome() 


def zap():  
    navegador.get("https://web.whatsapp.com/")
    time.sleep(5)

    esperate =navegador.find_elements("id",'side')
    while len(esperate) <1:
        time.sleep(1)
    print("entrando no novo whatsapp")    
    numero = number_for_response
    texto = "text_send"
    mensagem:str = urllib.parse.quote(texto)
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    #navegador.find_element('xpath', '//*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div/div[1]/div/div/div/img').click()
    #navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys("Olá, já falei que TE AMO hoje?").send_keys(Keys.ENTER)
    navegador.get(link)
    while len(esperate) < 1:
        time.sleep(1)
    navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
    time.sleep(5)
print("fim de programa")
zap()
while True:
    zap()
    tempo = 5
    print(f'tempo de espera {tempo} minutos...')
    time.sleep(tempo)





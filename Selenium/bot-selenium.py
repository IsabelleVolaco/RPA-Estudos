''' 
O selenium é uma ferramente que permite o controle do mouse e teclado do computador, ou seja, da minha própria máquina. Permite utilizar bots para navegar na internet, realizando tarefas.
>pip install selenium
>verificar versão do navegador, utilizei Chrome versão 122.0.6261.112 x64 bits
>chromedriver para windows x64 + colocá-lo no phyton.exe


# 1. abrir planilha / ferramenta / sistema / programa > tecla win + login.xlsx
# 2. preencher login
# 3. preencher senha
# 4. clicar em fazer login

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

navegador = webdriver.Chrome()

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.quit()
#1.


#2.

#3.


#4.
'''
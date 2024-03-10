''' 
O selenium é uma ferramente que permite o controle do mouse e teclado do computador, ou seja, da minha própria máquina. Permite utilizar bots para navegar na internet, realizando tarefas.
>pip install selenium
>verificar versão do navegador, utilizei Microsoft Edge versão 122.0.2365.80 (x64 bits)
>edgedriver para windows x64 + colocá-lo no phyton.exe
'''

from selenium import webdriver
#import time

browser = webdriver.Edge()
browser.get('https://petitgato.com.br/img/webp/gatos-persas-em-sao-paulo-img-3780.webp')
input()
#time.sleep(5)
#browser.quit()

#1.


#2.

#3.


#4.

#https://learn.microsoft.com/pt-br/microsoft-edge/webdriver-chromium/?tabs=python
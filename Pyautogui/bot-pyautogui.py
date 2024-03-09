''' 
O pyautogui é uma biblioteca que permite o controle do mouse e teclado do computador
>pip install pyautogui
'''

# 1. abrir planilha / ferramenta / sistema / programa > tecla win + login.xlsx
# 2. preencher login
# 3. preencher senha
# 4. clicar em fazer login

import pyautogui

pyautogui.PAUSE = 2 #Isso padroniza o tempo de espera antes da execução de cada comando, no caso, 2 segundos. Este seria o tempo de esperar o processamento dos comandos, pois como ele executa imediatamente, durante a automação pode ser que seja executado "um comando sobre outro", prejudicando o processo.

#1.
pyautogui.press("win") 
pyautogui.write("Login.xlsx")
pyautogui.press("enter")

#2.
pyautogui.click(x=444, y=281)
pyautogui.write("Isabelle")

#3.
pyautogui.click(x=444, y=317)
pyautogui.write("123")

#4.
pyautogui.click(x=444, y=436)
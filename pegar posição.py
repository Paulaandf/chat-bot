import time
import pyautogui

time.sleep(0.5)
print(pyautogui.position())
 



from selenium import webdriver

# Inicializa o browser
driver = webdriver.Chrome()

# Abre o site desejado
driver.get('https://www.smsolucoesdigital.com.br/index.html#/atendimentos/chat')

# Obtém a largura e altura do site
width = driver.execute_script("return document.body.scrollWidth")
height = driver.execute_script("return document.body.scrollHeight")

# Imprime a largura e altura do site
print("Largura do site:", width)
print("Altura do site:", height)

# Fecha o navegador
driver.quit()
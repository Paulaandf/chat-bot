import pyautogui
import time
pyautogui.PAUSE = 2
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# abrir o navegador (chrome)

pyautogui.press ("win")
pyautogui.write ("edge")
pyautogui.press("enter")
link = "https://www.smsolucoesdigital.com.br/index.html#/atendimentos/chat"
pyautogui.write (link)
pyautogui.press("enter")
time.sleep(3)
# entrar no link 
import pandas

tabela = pandas.read_excel("base.xlsx")
# Passo 2: Fazer login
for linha in tabela.index:
    pyautogui.click (x=116, y=163)
    pyautogui.write(str(tabela.loc[linha,"Número Celular"]))
    pyautogui.press("enter")    
    
    time.sleep(1)


import openai

chave_api = "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"
openai.api_key = chave_api
pyautogui.click (x=249, y=283)
import openai

chave_api = "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"
openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )

    return resposta["choices"][0]["message"]

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot:", resposta["content"])
# print(enviar_mensagem("Em que ano Eistein publicou a teoria geral da relatividade?"))
# Passo 1, entrar no sistema da empresa
# Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Preencher o formulário de login
# Passo 3 - Importar a base de dados
# Passo 4, cadastrar os produtos
# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time
from decimal import Decimal


# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - pressionar uma tecla
# pyautogui.hotkey - atalho do teclado/combinação de teclas
# pyautogui.scroll - rolar o scroll do mouse
# pyautogui.PAUSE = 0.5
# Documentação: https://pyautogui.readthedocs.io/en/latest/

# Passo 1 - Entrar no sistema
# Abrir o navegador
time.sleep(3)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.sleep(3) # o mesmo que time.sleep(3)

# Passo 2 - Preencher o formulário de login
pyautogui.press("tab")
# OU se fosse para fazer do jeito do profesor:
# pyautogui.click(x = 890, y = 357)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pedrogamer258@gmail.com")
pyautogui.press("tab")
pyautogui.write("'p1590236487'")
pyautogui.press("enter")
pyautogui.sleep(3)

# Passo 3 - Importar a base de dados
import pandas 
tabela = pandas.read_csv("produtos.csv")
# print(tabela)

# Passo 4, cadastrar os produtos
ps_codigo_x=805 
ps_codigo_y=242
# para cada linha da minha tabela:
for linha in tabela.index: 
# número da linha é chamado de index, "linha" poderia ser qualquer palavra
# o importante é que ele vai agir como um indíce e vai incrementando a cada iteração
    # codigo
    pyautogui.click(ps_codigo_x, ps_codigo_y)
    codigo = str(tabela.loc[linha, "codigo"]) # loc para localizar o item na tabela 
    # linha é a linha da tabela e "codigo" é o nome da coluna
    pyautogui.write(codigo) # vai escrever o texto da variável "codigo" no campo
    # marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    # tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    # categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    # preco_unitario
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    # custo_do_produto
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    # scroll
    pyautogui.scroll(1000)
    # OU
    # pyautogui.press("pageup")

# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

# Link par transformar o arquivo em .exe: https://youtu.be/cGSerUmK0CE?si=tp9sElLQ_oHTEuKS
# Link para automação web: https://youtu.be/8AMNaVt0z_M?si=J7i7Z2Vv6ox5J_US
# Link para rodar semanalmente: https://youtu.be/SxEjHAlCqmo?si=9K3ccaSgK8lq-iY2
# Link para rodar com PC desligado: https://youtu.be/-Wro4N9qWEQ?si=XCXjXpo9SkAmJBZ-

import pyautogui, time, pandas


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(3368, 491)
pyautogui.write("pythonimpressionador@gmail.com")

    

pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)

for linha in tabela.index:
    pyautogui.click(3356, 359)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
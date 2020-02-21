import pyautogui
"""
    Código pessoal para adicionar música no spotify para playlist soundtrack. 
"""

# x = [1038, 1139, 923, 1103, 730, 516]
# y = [593, 615, 708, 646, 680, 740]

xy = [
        (1038, 593),    # Posição: ... (3 pontos da segunda música de baixo para cima)
        (1139, 615),    # Posição: Adicionar á playlist
        (923, 708),     # Posição: Soundtrack
        (1103, 646),    # Posição: Seta descer lista
        (730, 680),     # Posição: Próxima música
        (516, 740),     # Posição: Powershell barra de tarefas
      ]


def go_and_click(x, y):
    """
        Vai para posição passada e clica com mouse.
    """
    pyautogui.moveTo(x, y, duration=0.3) 
    # posição não foi passada no click por um bug, onde o mesmo não clicava
    pyautogui.click(pyautogui.position()) 


for i in range(0, len(xy)):
    x, y = xy[i][0], xy[i][1]
    go_and_click(x, y)

pyautogui.hotkey('up') # seta para cima volta para último comando
pyautogui.moveTo(571, 550) # Posição: Em cima da próxima música

pyautogui.press
# https://automatetheboringstuff.com/chapter18/
# https://imasters.com.br/back-end/automacao-de-gui-com-python-exemplo-de-uso-do-pyautogui-2
# https://pyautogui.readthedocs.io/en/latest/

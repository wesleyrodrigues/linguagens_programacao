import pyautogui
x = [1038, 1139, 923, 1038, 1146, 730, 563] 
y = [593, 615, 680, 593, 646, 680, 747]

def go_and_click(x, y):
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click(pyautogui.position())

for i in range(0, len(x)):
    go_and_click(x[i], y[i])

# https://automatetheboringstuff.com/chapter18/
# https://imasters.com.br/back-end/automacao-de-gui-com-python-exemplo-de-uso-do-pyautogui-2
# https://pyautogui.readthedocs.io/en/latest/
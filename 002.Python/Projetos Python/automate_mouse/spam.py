import pyautogui
for i in range(0, 100):
    pyautogui.moveTo(705, 694)
    pyautogui.click(pyautogui.position())
    pyautogui.typewrite("Spam! "*3)
    pyautogui.hotkey('enter')

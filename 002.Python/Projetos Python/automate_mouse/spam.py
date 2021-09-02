import pyautogui
l = "Spam Spam Spam."

for i in range(1, len(l)):
    pyautogui.moveTo(705, 694)
    pyautogui.click(pyautogui.position())
    if (not(l[i] == " ")):
        pyautogui.typewrite(l[:i]) # l[:i]
        pyautogui.hotkey('enter')

import pyautogui, time
 
# time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
# distance = 200
tam = 200
pyautogui.dragRel(tam, 0, duration=0.2)
pyautogui.dragRel(0, tam, duration=0.2)
pyautogui.dragRel(-tam, 0, duration=0.2)
pyautogui.dragRel(0, -tam, duration=0.2)
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=0.2)# move right
#     distance = distance - 5
#     pyautogui.dragRel(0, distance, duration=0.2)# move down
#     pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
#     distance = distance - 5
#     pyautogui.dragRel(0, -distance, duration=0.2)  # move up

# https://automatetheboringstuff.com/chapter18/
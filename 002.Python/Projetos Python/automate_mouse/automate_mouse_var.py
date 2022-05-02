import pyautogui as pya
# x = [] 
# y = []

def go_and_click(x, y, but, cli, dur=0.3):
    pya.moveTo(x, y, duration=dur)
    if(cli):
        pya.click(pya.position(), button=but)

go_and_click(41, 676, "right", True)
go_and_click(107, 603, "left", False)
go_and_click(336, 672, "left", False, 0.5)
pya.scroll(-200)
pya.click(pya.position(), duration=0.5)
go_and_click(41, 676, "right", True)
go_and_click(109, 561, "left", True)
go_and_click(723, 659, "left", True)
go_and_click(752, 387, "left", False)
pya.scroll(-100)




# go_and_click(277, 601, "right", False)
# go_and_click(460, 581, "right", False)
# pya.scroll(-200)
# go_and_click(485, 663, "left", True)
# go_and_click(49, 675, "right", True)
# go_and_click(238, 550, "right", True)



# pya.moveTo(277, 601, duration=0.3)

# for i in range(0, len(x)):
#     go_and_click(x[i], y[i], "left")
# pya.hotkey('up')
# pya.moveTo(571, 550)

# https://automatetheboringstuff.com/chapter18/
# https://imasters.com.br/back-end/automacao-de-gui-com-python-exemplo-de-uso-do-pya-2
# https://pya.readthedocs.io/en/latest/


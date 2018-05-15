import win32api, win32con, time
from Point import *
from MouseUtils import *

def click():
    # print("User still active")
    # time.sleep(290)

    init_pos = getMousePosition()
    while True:
        new_pos = getMousePosition()
        if (init_pos.x == new_pos.x or init_pos.y == new_pos.y):
            print("User inactive - Mouse moved")
            new_pos.setPoints(x = int(1920/4 * 3),y = (1080-20))
            moveMouseToPos(init_pos, new_pos, 0.5)
        else:
            print("User still active")

        init_pos = new_pos
        time.sleep(100)

click()

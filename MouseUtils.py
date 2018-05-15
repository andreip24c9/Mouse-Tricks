from ctypes import windll, byref
from Point import *
from time import sleep
import win32api, win32con

def getMousePosition():
    pt = Point()
    windll.user32.GetCursorPos(byref(pt))
    return pt

def clickMouseLeftBtn(x, y):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def moveMouseToPos(fromPoint, toPoint, durationSec):
    deltaX = toPoint.x - fromPoint.x
    deltaY = toPoint.y - fromPoint.y
    # deltaY = 0

    totalDistancePx = abs(deltaX) + abs(deltaY)
    distance = deltaX - 1

    noAnimFrames = totalDistancePx/(durationSec * 30)
    i = 0;
    while (totalDistancePx > abs(deltaY)):
        new_x_pos = fromPoint.x + deltaX - distance
        if(i == int(noAnimFrames)):
            i = 0;
            # update ui every noAminFrames frames
            win32api.SetCursorPos((new_x_pos,fromPoint.y))
            sleep(1/60)
        i += 1;
        totalDistancePx -= 1

        if (distance > 0) :
            distance -= 1
        else :
            distance += 1

    i = 0;
    distance = deltaY - 1
    while (totalDistancePx > 0):
        new_y_pos = fromPoint.y + deltaY - distance
        if(i == int(noAnimFrames)):
            i = 0;
            # update ui every noAminFrames frames
            win32api.SetCursorPos((toPoint.x,new_y_pos))
            sleep(1/60)
        i += 1;
        totalDistancePx -= 1

        if (distance > 0) :
            distance -= 1
        else :
            distance += 1

    win32api.SetCursorPos((toPoint.x,toPoint.y))
    clickMouseLeftBtn(toPoint.x,toPoint.y)

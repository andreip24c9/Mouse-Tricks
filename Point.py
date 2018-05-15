from ctypes import Structure, c_long

class Point(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

    def __init__(self):
        self.x = 0
        self.y = 0

    def setPoints(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        print("x = %s, y = %s" % (self.x, self.y))

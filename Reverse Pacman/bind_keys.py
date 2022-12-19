from graphics import *
import time

# --- classes ---

class Player:
    def __init__(self, window, char):
        self.p1 = char
        self.win = window

    def create(self):
        self.p1.setFill("blue")
        self.p1.draw(self.win)

    def movement(self):
        if self.win.lastKey == "d":
            self.p1.move(10, 0)
        if self.win.lastKey == "a":
            self.p1.move(-10, 0)
        if self.win.lastKey == "s":
            self.p1.move(0, 10)
        if self.win.lastKey == "w":
            self.p1.move(0, -10)
            
    def block(self):
        self.p1.move(0,0)
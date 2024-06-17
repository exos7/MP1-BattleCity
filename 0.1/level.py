import pyxel
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

class Level_1:
    def __init__(self):
        self.coords = [
            Point(0, 112), 
            Point(0, 120), 
            Point(16, 16), 
            Point(16, 32),
            Point(16, 32),
            Point(16, 48),
            Point(16, 64),
            Point(16, 80),
            Point(16, 144),
            Point(16, 160),
            Point(16, 176),
            ]

    def update(self):
        pass

    def draw(self):
        #0th Column
        pyxel.blt(0, 112, 0, 0, 16, 16, 8)
        pyxel.blt(0, 120, 0 , 0 , 0 , 16, 8)
        #1st Column
        pyxel.blt(16, 16, 0, 0, 16, 16, 16)
        pyxel.blt(16, 32, 0, 0, 16, 16, 16)
        pyxel.blt(16, 48, 0, 0, 16, 16, 16)
        pyxel.blt(16, 64, 0, 0, 16, 16, 16)
        pyxel.blt(16, 80, 0, 0, 16, 16, 16)
        pyxel.blt(16, 144, 0, 0, 16, 16, 16)
        pyxel.blt(16, 160, 0, 0, 16, 16, 16)
        pyxel.blt(16, 176, 0, 0, 16, 16, 16)
        #2nd Column
        pyxel.blt(32, 112, 0, 0, 16, 16, 16)
        #3rd Column
        pyxel.blt(48, 16, 0, 0, 16, 16, 16)
        pyxel.blt(48, 32, 0, 0, 16, 16, 16)
        pyxel.blt(48, 48, 0, 0, 16, 16, 16)
        pyxel.blt(48, 64, 0, 0, 16, 16, 16)
        pyxel.blt(48, 80, 0, 0, 16, 16, 16)
        pyxel.blt(48, 112, 0, 0, 16, 16, 16)
        pyxel.blt(48, 144, 0, 0, 16, 16, 16)
        pyxel.blt(48, 160, 0, 0, 16, 16, 16)
        pyxel.blt(48, 176, 0, 0, 16, 16, 16)
        #5th Column
        pyxel.blt(80, 16, 0, 0, 16, 16, 16)
        pyxel.blt(80, 32, 0, 0, 16, 16, 16)
        pyxel.blt(80, 48, 0, 0, 16, 16, 16)
        pyxel.blt(80, 64, 0, 0, 16, 16, 8)
        pyxel.blt(80, 96, 0, 0, 16, 16, 16)
        pyxel.blt(80, 128, 0, 0, 16, 16, 16)
        pyxel.blt(80, 144, 0, 0, 16, 16, 16)
        pyxel.blt(80, 160, 0, 0, 16, 16, 16)
        #6th Column
        pyxel.blt(96, 48, 0, 0, 0 ,16, 16)
        pyxel.blt(96, 136, 0, 0, 16 ,16, 8)
        pyxel.blt(96, 144, 0, 0, 16 ,16, 16)
        #7th Column
        pyxel.blt(112, 16, 0, 0, 16, 16, 16)
        pyxel.blt(112, 32, 0, 0, 16, 16, 16)
        pyxel.blt(112, 48, 0, 0, 16, 16, 16)
        pyxel.blt(112, 64, 0, 0, 16, 16, 8)
        pyxel.blt(112, 96, 0, 0, 16, 16, 16)
        pyxel.blt(112, 128, 0, 0, 16, 16, 16)
        pyxel.blt(112, 144, 0, 0, 16, 16, 16)
        pyxel.blt(112, 160, 0, 0, 16, 16, 16)
        #9th Column
        pyxel.blt(144, 16, 0, 0, 16, 16, 16)
        pyxel.blt(144, 32, 0, 0, 16, 16, 16)
        pyxel.blt(144, 48, 0, 0, 16, 16, 16)
        pyxel.blt(144, 64, 0, 0, 16, 16, 16)
        pyxel.blt(144, 80, 0, 0, 16, 16, 16)
        pyxel.blt(144, 112, 0, 0, 16, 16, 16)
        pyxel.blt(144, 144, 0, 0, 16, 16, 16)
        pyxel.blt(144, 160, 0, 0, 16, 16, 16)
        pyxel.blt(144, 176, 0, 0, 16, 16, 16)
        #10th Column
        pyxel.blt(160, 112, 0, 0, 16, 16, 16)
        #11th Column
        pyxel.blt(176, 16, 0, 0, 16, 16, 16)
        pyxel.blt(176, 32, 0, 0, 16, 16, 16)
        pyxel.blt(176, 48, 0, 0, 16, 16, 16)
        pyxel.blt(176, 64, 0, 0, 16, 16, 16)
        pyxel.blt(176, 80, 0, 0, 16, 16, 16)
        pyxel.blt(176, 144, 0, 0, 16, 16, 16)
        pyxel.blt(176, 160, 0, 0, 16, 16, 16)
        pyxel.blt(176, 176, 0, 0, 16, 16, 16)
        #12th Column
        pyxel.blt(192, 112, 0, 0, 16, 16, 8)
        pyxel.blt(192, 120, 0 , 0 , 0 , 16, 8)
import pyxel
from dataclasses import dataclass
from block import Block

@dataclass
class Point:
    x: int
    y: int
    type: str

class Level_1:
    def __init__(self):
        self.coords = [
            Point(0, 112, 'HORI_HALF_BRICK'), 
            Point(0, 120, 'HORI_HALF_STONE'), 
            Point(16, 16, 'BRICK'), 
            Point(16, 32, 'BRICK'),
            Point(16, 32, 'BRICK'),
            Point(16, 48, 'BRICK'),
            Point(16, 64, 'BRICK'),
            Point(16, 80, 'BRICK'),
            Point(16, 144, 'BRICK'),
            Point(16, 160, 'BRICK'),
            Point(16, 176, 'BRICK'),
            Point(32, 112, 'BRICK'),
            Point(48, 16, 'BRICK'),
            Point(48, 32, 'BRICK'),
            Point(48, 48, 'BRICK'),
            Point(48, 64, 'BRICK'),
            Point(48, 80, 'BRICK'),
            Point(48, 112, 'BRICK'),
            Point(48, 144, 'BRICK'),
            Point(48, 160, 'BRICK'),
            Point(48, 176, 'BRICK'),
            #5th Column
            Point(80, 16, 'BRICK'),
            Point(80, 32, 'BRICK'),
            Point(80, 48, 'BRICK'),
            Point(80, 64, 'HORI_HALF_BRICK'),
            Point(80, 96, 'BRICK'),
            Point(80, 128, 'BRICK'),
            Point(80, 144, 'BRICK'),
            Point(80, 160, 'BRICK'),
            #6th Column
            Point(96, 48, 'STONE'),
            Point(96, 136, 'HORI_HALF_BRICK'),
            Point(96, 144, 'BRICK'),
            #7th Column
            Point(112, 16, 'BRICK'),
            Point(112, 32, 'BRICK'),
            Point(112, 48, 'BRICK'),
            Point(112, 64,'HORI_HALF_BRICK'),
            Point(112, 96, 'BRICK'),
            Point(112, 128, 'BRICK'),
            Point(112, 144, 'BRICK'),
            Point(112, 160, 'BRICK'),
            #9th Column
            Point(144, 16, 'BRICK'),
            Point(144, 32, 'BRICK'),
            Point(144, 48, 'BRICK'),
            Point(144, 64, 'BRICK'),
            Point(144, 80, 'BRICK'),
            Point(144, 112, 'BRICK'),
            Point(144, 144, 'BRICK'),
            Point(144, 160, 'BRICK'),
            Point(144, 176, 'BRICK'),
            #10th Column
            Point(160, 112, 'BRICK'),
            #11th Column
            Point(176, 16, 'BRICK'),
            Point(176, 32, 'BRICK'),
            Point(176, 48, 'BRICK'),
            Point(176, 64, 'BRICK'),
            Point(176, 80, 'BRICK'),
            Point(176, 144, 'BRICK'),
            Point(176, 160, 'BRICK'),
            Point(176, 176, 'BRICK'),
            #12th Column
            Point(192, 112,'HORI_HALF_BRICK'),
            Point(192, 120, 'HORI_HALF_STONE'),
            ]
        
    def update(self):
        pass

    def draw(self):
        for i in range(len(self.coords)):
            # print('working')
            x = Block(self.coords[i])
            x.draw()
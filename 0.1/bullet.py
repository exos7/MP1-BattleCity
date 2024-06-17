import pyxel
from functions import in_bounds

BULLET_WIDTH = 2
BULLET_HEIGHT = 2

class Bullet:
    def __init__(self, x, y, facing, isPlayer):
        self.facing = facing
        self.x = x
        self.y = y
        if self.facing == 0:
            self.y -= 8
        if self.facing == 1:
            self.x += 8
        if self.facing == 2:
            self.y += 8
        if self.facing == 3:
            self.x -= 8
        self.u = 32
        self.v = 0
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.isAlive = True
        self.isPlayer = isPlayer


    def update(self):
        if self.facing == 0:
            self.y -= 4
            self.u = 32
            self.v = 0
        if self.facing == 1:
            self.x += 4
            self.u = 40
            self.v = 0
        if self.facing == 2:
            self.u = 32
            self.v = 8
            self.y += 4
        if self.facing == 3:
            self.u = 40
            self.v = 8
            self.x -= 4
        if in_bounds(self.x, self.y):
            self.isAlive = True
        else:
            self.isAlive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, 4, 4)
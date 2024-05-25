import pyxel
from functions import in_bounds

BULLET_WIDTH = 2
BULLET_HEIGHT = 2

class Bullet:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.facing = facing
        self.isAlive = True

    def update(self):
        if self.facing == 0:
            self.y -= 4
        if self.facing == 1:
            self.x += 4
        if self.facing == 2:
            self.y += 4
        if self.facing == 3:
            self.x -= 4

        if in_bounds(self.x, self.y):
            self.isAlive = False

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 5)
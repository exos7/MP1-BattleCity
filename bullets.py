import pyxel
from settings import bulletSpeed
class Bullet:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        if self.facing == 0:
            self.u, self.v = 32, 0
            self.x += 6
            self.y -= 2
        elif self.facing == 1:
            self.u, self.v = 40, 0
            self.x += 16
            self.y += 6
        elif self.facing == 2:
            self.u, self.v = 32, 8
            self.x += 6
            self.y += 16
        elif self.facing == 3:
            self.u, self.v = 40, 8
            self.y += 6
            self.x -= 2
        self.width = 4
        self.height = 4
    
    def update(self):
        if self.facing == 0:
            self.y -= bulletSpeed
        elif self.facing == 1:
            self.x += bulletSpeed
        elif self.facing == 2:
            self.y += bulletSpeed
        elif self.facing == 3:
            self.x -= bulletSpeed
    
    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.width, self.height)
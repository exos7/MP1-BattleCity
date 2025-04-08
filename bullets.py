import pyxel
from settings import bulletSpeed
class Bullet:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        if self.facing == 0:
            self.u, self.v = 32, 0
            self.x += 8
            self.y -= 2
        elif self.facing == 1:
            self.u, self.v = 40, 0
            self.x += 18
            self.y += 8
        elif self.facing == 2:
            self.u, self.v = 32, 8
            self.x += 8
            self.y += 18
        elif self.facing == 3:
            self.u, self.v = 40, 8
            self.y += 8
            self.x -= 2
        self.width = 1
        self.height = 1
    
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
        pyxel.circ(self.x, self.y, self.width, 13)
import pyxel

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.isAlive = True
        self.facing = 0
        self.isShooting = False
    
    def update(self):
        if self.facing == 0:
            self.u, self.v = 0, 0
        elif self.facing == 1:
            self.u, self.v = 16, 0
        elif self.facing == 2:
            self.u, self.v = 0, 16
        elif self.facing == 3:
            self.u, self.v = 16, 16

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, self.u, self.v, 16, 16)
import pyxel

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.isAlive = True
        self.facing = 0
        self.isShooting = False
        self.width = 16
        self.height = 16
        self.bullets = []
        self.health = 3
        
    
    def update(self):
        if self.facing == 0:
            self.u, self.v = 0, 64
        elif self.facing == 1:
            self.u, self.v = 16, 64
        elif self.facing == 2:
            self.u, self.v = 0, 80
        elif self.facing == 3:
            self.u, self.v = 16, 80

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, self.u, self.v, 16, 16, 0)
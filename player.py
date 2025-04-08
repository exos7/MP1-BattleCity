import pyxel

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.life = 3
        self.isAlive = True
        self.canMove = True
        self.facing = 0
        self.isShooting = False
        self.width = 16
        self.height = 16
        self.bullets = []
        self.lives = 3
        self.killsForPowerups = 0
        self.shields = []
        self.isShielded = False
        
    
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
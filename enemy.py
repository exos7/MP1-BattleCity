import pyxel
import random
from functions import inBounds
from settings import moveSpeed

class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = True
        self.facing = 0
        self.isShooting = False
        self.width = 16
        self.height = 16
        self.bullets = []
        
    
    def update(self):
        pass

    def draw(self):
        pass

class Blue(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.u, self.v = 0, 0
        self.health = 10
        self.type = 'blue'
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
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.height, self.width, 0)

class Red(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.u, self.v = 0, 32
        self.health = 20
        self.type = 'red'
    
    def update(self):
        
            if self.facing == 0:
                self.u, self.v = 0, 32
            elif self.facing == 1:
                self.u, self.v = 16, 32
            elif self.facing == 2:
                self.u, self.v = 0, 48
            elif self.facing == 3:
                self.u, self.v = 16, 48
        
    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.height, self.width, 0)
    
class Green(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.u, self.v = 0, 64
        self.health = 20
        self.type = 'green'
    
    def update(self):
            if self.facing == 0:
                self.u, self.v = 0, 96
            elif self.facing == 1:
                self.u, self.v = 16, 96
            elif self.facing == 2:
                self.u, self.v = 0, 112
            elif self.facing == 3:
                self.u, self.v = 16, 112
        
    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.height, self.width, 0)

class Yellow(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.u, self.v = 0, 128
        self.health = 20
        self.type = 'yellow'
    
    def update(self):
            if self.facing == 0:
                self.u, self.v = 0, 128
            elif self.facing == 1:
                self.u, self.v = 16, 128
            elif self.facing == 2:
                self.u, self.v = 0, 144
            elif self.facing == 3:
                self.u, self.v = 16, 144
        
    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.height, self.width, 0)

class Purple(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.u, self.v = 0, 160
        self.health = 20
        self.type = 'purple'
    
    def update(self):
            if self.facing == 0:
                self.u, self.v = 0, 160
            elif self.facing == 1:
                self.u, self.v = 16, 160
            elif self.facing == 2:
                self.u, self.v = 0, 176
            elif self.facing == 3:
                self.u, self.v = 16, 176
        
    def draw(self):
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.height, self.width, 0)
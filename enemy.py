from functions import atBottom, atTop, atLeft, atRight
import random
import pyxel

MoveSpeed = 4

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.isAlive = True
        self.Dir = 0

    def in_bounds(self, x, y):
        if 0 <= x <= pyxel.width and 0 <= y <= pyxel.height:
            return True

    def update(self):
        if pyxel.frame_count % 20 == 0:
            NewDir = random.randint(0, 3) 
            self.Dir = NewDir
        DirInt = self.Dir
        # DirInt = random.randint(0, 3) 
        if self.in_bounds(self.x, self.y):
            if DirInt == 0 and not atTop(self.x, self.y):
                self.u = 0
                self.v = 32
                self.y -= MoveSpeed
            if DirInt == 1 and not atLeft(self.x, self.y):
                self.u = 16
                self.v = 48
                self.x -= MoveSpeed
            if DirInt == 2 and not atBottom(self.x, self.y):
                self.u = 0
                self.v = 48
                self.y += MoveSpeed
            if DirInt == 3 and not atRight(self.x, self.y):
                self.u = 16
                self.v = 32
                self.x += MoveSpeed
        
            
                  
    def draw(self):
        # pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, self.u, self.v, 16, 16)

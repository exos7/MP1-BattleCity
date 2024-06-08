from functions import atBottom, atTop, atLeft, atRight
from level import Level_1, Point
import random
import pyxel

MoveSpeed = 2

class Enemy:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.isAlive = True
        self.Dir = 0
        self.isShooting = False
        self.num = num
        self.givenpts = Level_1().coords
        self.unmovable: list[tuple[int,int]] = []
        for point in self.givenpts:
            x = point.x
            y = point.y
            for i in range(x-15, x+16):
               for j in range(y-15, y+16):
                    self.unmovable.append((i,j))
        # print(self.unmovable)

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
                if (self.x, self.y - MoveSpeed) in self.unmovable:
                    self.y -= 0
                else:
                    self.y -= MoveSpeed
            if DirInt == 1 and not atLeft(self.x, self.y):
                self.u = 16
                self.v = 48
                if (self.x - MoveSpeed, self.y) in self.unmovable:
                    self.x -= 0
                else:
                    self.x -= MoveSpeed
            if DirInt == 2 and not atBottom(self.x, self.y):
                self.u = 0
                self.v = 48
                if (self.x, self.y+16) in self.unmovable:
                    self.y += 0
                else:
                    self.y += MoveSpeed

            if DirInt == 3 and not atRight(self.x, self.y):
                self.u = 16
                self.v = 32
                if (self.x+16, self.y) in self.unmovable:
                    self.x += 0
                else:
                    self.x += MoveSpeed
        
            
                  
    def draw(self):
        if self.isAlive == False:
            pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, self.u, self.v, 16, 16)

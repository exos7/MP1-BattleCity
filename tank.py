from functions import atBottom, atTop, atLeft, atRight, in_bounds
from level import Level_1, Point
import pyxel

MoveSpeed = 2

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.isAlive = True
        self.facing = 0 # 0 - up, 1 - right, 2 - down, 3 - left
        self.isShooting = 0
        self.givenpts = Level_1().coords
        self.unmovable: list[tuple[int,int]] = []
        for point in self.givenpts:
            x = point.x
            y = point.y
            for i in range(x-15, x+16):
               for j in range(y-15, y+16):
                    self.unmovable.append((i,j))
        # print(self.unmovable)


    def update(self):
        click = False
        if in_bounds(self.x, self.y):
                if pyxel.btn(pyxel.KEY_W) and not atTop(self.x, self.y) and not click :
                    print(self.x, self.y)
                    # print('w')
                    self.u = 0
                    self.v = 0
                    # self.y -= MoveSpeed
                    click = True
                    self.facing = 0

                    if (self.x, self.y - MoveSpeed) in self.unmovable:
                        self.y -= 0
                    else:
                        self.y -= MoveSpeed

                if pyxel.btn(pyxel.KEY_A) and not atLeft(self.x, self.y) and not click:
                    print(self.x, self.y)
                    # print('a')
                    self.u = 16
                    self.v = 16
                    # self.x -= MoveSpeed
                    click = True
                    self.facing = 3
                    if (self.x - MoveSpeed, self.y) in self.unmovable:
                        self.x -= 0
                    else:
                        self.x -= MoveSpeed

                if pyxel.btn(pyxel.KEY_S) and not atBottom(self.x, self.y) and not click:
                    print(self.x, self.y)
                    # print('s')
                    self.u = 0
                    self.v = 16
                    # self.y += MoveSpeed
                    click = True
                    self.facing = 2
                    if (self.x, self.y+16) in self.unmovable:
                        self.y += 0
                    else:
                        self.y += MoveSpeed

                if pyxel.btn(pyxel.KEY_D) and not atRight(self.x, self.y) and not click:
                    print(self.x, self.y)
                    # print('d')
                    self.u = 16
                    self.v = 0
                    # self.x += MoveSpeed
                    click = True
                    self.facing = 1
                    if (self.x+16, self.y) in self.unmovable:
                        self.x += 0
                    else:
                        self.x += MoveSpeed
                    
    def draw(self):
        pyxel.cls(0)
        if self.isAlive:
            pyxel.blt(self.x, self.y, 1, self.u, self.v, 16, 16)


# if self.blocks:
            #     for block in self.blocks:
            #         #tank is above block
            #         if self.tank.y == block.y+1:
            #             self.tank.speedS = 0
            #             print('above')
            #         else: 
            #             self.tank.speedS = MoveSpeed

            #         #tank is to the left of block
            #         if self.tank.x == block.x-1:
            #             self.tank.speedD = 0
            #             print('left')
            #         else: 
            #             self.tank.speedD = MoveSpeed

            #         #tank is below block
            #         if self.tank.y == block.y-1:
            #             print('below')
            #             self.tank.speedW = 0
            #         else: 
            #             self.tank.speedW = MoveSpeed

            #         #tank is to the right of block
            #         if self.tank.x == block.x+1:
            #             print('right')
            #             self.tank.speedA = 0
            #         else: 
            #             self.tank.speedA = MoveSpeed
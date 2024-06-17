from functions import atBottom, atTop, atLeft, atRight, in_bounds, is_colliding
import pyxel

MoveSpeed = 2


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.isAlive = True
        self.facing = 0 # 0 - up, 1 - right, 2 - down, 3 - left
        self.isShooting = 0

    def update(self):
        click = False
        if in_bounds(self.x, self.y):
            if pyxel.btn(pyxel.KEY_W) and not atTop(self.x, self.y) and not click:
                # print('w')
                self.u = 0
                self.v = 0
                self.y -= MoveSpeed
                click = True
                self.facing = 0
            if pyxel.btn(pyxel.KEY_A) and not atLeft(self.x, self.y) and not click:
                # print('a')
                self.u = 16
                self.v = 16
                self.x -= MoveSpeed
                click = True
                self.facing = 3
            if pyxel.btn(pyxel.KEY_S) and not atBottom(self.x, self.y) and not click:
                # print('s')
                self.u = 0
                self.v = 16
                self.y += MoveSpeed
                click = True
                self.facing = 2
            if pyxel.btn(pyxel.KEY_D) and not atRight(self.x, self.y) and not click:
                # print('d')
                self.u = 16
                self.v = 0
                self.x += MoveSpeed
                click = True
                self.facing = 1
                  
    def draw(self):
        pyxel.cls(0)
        if self.isAlive:
            pyxel.blt(self.x, self.y, 1, self.u, self.v, 16, 16)

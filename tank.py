from functions import atBottom, atTop, atLeft, atRight
import pyxel

MoveSpeed = 4

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0
        self.isAlive = True

    def in_bounds(self, x, y):
        if 0 <= x <= pyxel.width and 0 <= y <= pyxel.height:
            return True

    def update(self):
        click = False
        if self.in_bounds(self.x, self.y):
            if pyxel.btn(pyxel.KEY_W) and not atTop(self.x, self.y) and not click:
                print('w')
                self.u = 0
                self.v = 0
                self.y -= MoveSpeed
                click = True
            if pyxel.btn(pyxel.KEY_A) and not atLeft(self.x, self.y) and not click:
                print('a')
                self.u = 16
                self.v = 16
                self.x -= MoveSpeed
                click = True
            if pyxel.btn(pyxel.KEY_S) and not atBottom(self.x, self.y) and not click:
                print('s')
                self.u = 0
                self.v = 16
                self.y += MoveSpeed
                click = True
            if pyxel.btn(pyxel.KEY_D) and not atRight(self.x, self.y) and not click:
                print('d')
                self.u = 16
                self.v = 0
                self.x += MoveSpeed
                click = True
                  
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, self.u, self.v, 16, 16)

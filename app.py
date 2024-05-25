import pyxel

def atRight(x, y):
    if pyxel.width - 8 == x:
        return True

def atLeft(x, y):
    if 0 == x:
        return True

def atTop(x, y):
    if 0 == y:
        return True

def atBottom(x, y):
    if pyxel.height - 8 == y:
        return True

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
        if self.in_bounds(self.x, self.y):
            if pyxel.btn(pyxel.KEY_W) and not atTop(self.x, self.y):
                print('w')
                self.u = 0
                self.v = 0
                self.y -= 16
            if pyxel.btn(pyxel.KEY_A) and not atLeft(self.x, self.y):
                print('a')
                self.u = 16
                self.v = 16
                self.x -= 16
            if pyxel.btn(pyxel.KEY_S) and not atBottom(self.x, self.y):
                print('s')
                self.u = 0
                self.v = 16
                self.y += 16
            if pyxel.btn(pyxel.KEY_D) and not atRight(self.x, self.y):
                print('d')
                self.u = 16
                self.v = 0
                self.x += 16
                  
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, self.u, self.v, 16, 16)



class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        self.tank = Tank(self.x, self.y)
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.tank.isAlive == True:
            self.tank.update()
            if pyxel.btn(pyxel.KEY_SPACE):
                print('space')
                self.tank.draw()
    def draw(self):
        self.tank.draw()

App()
import pyxel

class Bullet:

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pyxel.circ(self.x, self.y, 8, 12)

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.u, self.v = 0, 0

    def in_bounds(self, x, y):
        if 0 <= x <= pyxel.width and 0 <= y <= pyxel.height:
            return True
    
    def update(self):
        if self.in_bounds(self.x, self.y):
            if pyxel.btn(pyxel.KEY_W):
                print("up")
                self.u = 0
                self.v = 0
                self.y -= 8
            if pyxel.btn(pyxel.KEY_A):
                print('left')
                self.u = 8
                self.v = 8
                self.x -= 8
            if pyxel.btn(pyxel.KEY_S):
                self.u = 0
                self.v = 8
                self.y += 8
            if pyxel.btn(pyxel.KEY_D):
                self.u = 8
                self.v = 0
                self.x += 8
            if pyxel.btnp(pyxel.KEY_SPACE):
                Bullet(self.x, self.y)
            
                 
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, self.u, self.v, 8, 8)



class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        self.tank = Tank(self.x, self.y)
        self.bullets = Bullet(self.x, self.y)
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tank.update()
        self.bullets.update()
    def draw(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.draw()
        self.tank.draw()

App()
import pyxel

class Blast:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1
        self.isAlive = True

    def update(self):
        self.radius += 1
        if self.radius > 8:
            self.isAlive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 7)
        pyxel.circb(self.x, self.y, self.radius, 10)
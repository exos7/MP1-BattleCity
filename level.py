import pyxel

class Screen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        # if pyxel.btn(pyxel.KEY_G):
        #     pyxel.cls(0)
        pass


    def draw(self):
        pyxel.rect(self.x, self.y, 200, 150, 13)
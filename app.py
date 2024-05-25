import pyxel
from tank import Tank

class App:
    def __init__(self):
        pyxel.init(320, 240)
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
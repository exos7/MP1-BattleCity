import pyxel
from tank import Tank
from enemy import Enemy

class App:
    def __init__(self):
        pyxel.init(320, 240)
        self.x = 0
        self.y = 0
        self.tank = Tank(self.x, self.y)
        self.enemy = Enemy(20,20)
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.tank.isAlive == True:
            self.tank.update()
            self.enemy.update()
    def draw(self):
        self.tank.draw()
        self.enemy.draw()
        # x.draw()

App()
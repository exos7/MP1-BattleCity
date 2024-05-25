import pyxel
from tank import Tank
from enemy import Enemy

class App:
    def __init__(self):
        pyxel.init(320, 240)
        self.x = 0
        self.y = 0
        self.tank = Tank(self.x, self.y)
        self.enemies = []
        
        for _ in range(5):
            self.enemies.append(Enemy(50, 50))
    
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.tank.isAlive == True:
            self.tank.update()
            for _ in self.enemies:
                _.update()
    def draw(self):
        self.tank.draw()
        for _ in self.enemies:
            _.draw()

App()
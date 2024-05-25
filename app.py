import pyxel
import random
from tank import Tank
from enemy import Enemy
from bullet import Bullet

 
class App:
    def __init__(self):
        pyxel.init(320, 240)
        self.x = 0
        self.y = 0
        self.tank = Tank(self.x, self.y)
        self.enemies = []
        self.bullets = []
        
        for _ in range(5):
            self.enemies.append(Enemy(48, 48))
    
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.tank.isAlive == True:
            self.tank.update()
            for enemy in self.enemies:
                enemy.update()
                willShoot = random.randint(0,40)
                enemyBullet = Bullet(enemy.x + (16/2), enemy.y + (16/2), enemy.Dir)
                if willShoot == 1:
                    self.bullets.append(enemyBullet)
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.bullets.append(Bullet(self.tank.x + (16/2), self.tank.y + (16/2), self.tank.facing))

            if self.bullets:
                for bullet in self.bullets:
                    bullet.update()
                    

    def draw(self):
        self.tank.draw()
        for enemy in self.enemies:
            enemy.draw()
        for bullet in self.bullets:
            bullet.draw()        
        

App()
import pyxel
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from functions import inBounds, isColliding
from blast import Blast
from level import Level_1


BULLET_FREQUENCY = 20

def entityUpdate(entities):
    for entity in entities:
        entity.update()
def entityDraw(entities):
    for entity in entities:
        entity.draw()

def levelDraw(level):
    level.draw()

class App:
    def __init__(self):
        pyxel.init(208, 208)
        self.x = 0
        self.y = 0
        self.tank = Player(self.x, self.y)
        self.enemies = []
        self.playerBullets = []
        self.bullets = []
        self.blasts = []
        # self.level_1 = Level_1()
    
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        for enemies in range(10):
            while len(self.enemies) < 5:
                self.enemies.append(Enemy(320//2, 240//2, enemies))

        if self.tank.isAlive == True or False:
            self.tank.update()    
            if pyxel.btnp(pyxel.KEY_SPACE) and not self.tank.isShooting:
                self.bullets.append(Bullet(self.tank.x + (16/2 + .5), self.tank.y + (16/2 + .5), self.tank.facing, True))
                self.tank.isShooting = True

            if self.enemies:
                for enemy in self.enemies:
                    enemy.update()
                    for bullet in self.bullets:
                        if not bullet.isAlive:
                            if bullet.isPlayer == True:
                                self.tank.isShooting = False
                            self.bullets.remove(bullet)
                        if isColliding(enemy, bullet) and isColliding(enemy, bullet) and bullet.isPlayer == True:
                            self.enemies.remove(enemy)
                            self.bullets.remove(bullet)
                            self.tank.isShooting = 0
                            self.blasts.append(Blast(enemy.x, enemy.y))
                            self.tank.isShooting = False
                        if isColliding(self.tank, bullet) and isColliding(self.tank, bullet):     
                            self.tank.isAlive = True
                            print('tank was hit')
                            self.bullets.remove(bullet)
                            self.tank.isShooting = False
                             
                    willShoot = random.randint(0, BULLET_FREQUENCY)
                    # willShoot = 0
                    enemyBullet = Bullet(enemy.x + (16/2), enemy.y + (16/2), enemy.Dir, False)
                    if willShoot == 1:
                        self.bullets.append(enemyBullet)
    
            if self.blasts:
                for blast in self.blasts:
                    if blast.isAlive == False:
                        self.blasts.remove(blast)
            if self.bullets:
                entityUpdate(self.bullets)
            
            if self.blasts:
                entityUpdate(self.blasts)

                

    def draw(self):
        self.tank.draw()
        entityDraw(self.enemies)
        entityDraw(self.bullets)
        entityDraw(self.blasts)

        # levelDraw(self.level_1)
        

App()
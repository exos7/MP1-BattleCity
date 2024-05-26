import pyxel
import random
from tank import Tank
from enemy import Enemy
from bullet import Bullet
from functions import in_bounds
from blast import Blast


BULLET_FREQUENCY = 20
 
class App:
    def __init__(self):
        pyxel.init(320, 240)
        self.x = 0
        self.y = 0
        self.tank = Tank(self.x, self.y)
        self.enemies = []
        self.bullets = []
        self.blasts = []
        
        for _ in range(5):
            self.enemies.append(Enemy(320//2, 240//2))
    
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):

        if self.tank.isAlive == True:
            self.tank.update()
            
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.bullets.append(Bullet(self.tank.x + (16/2), self.tank.y + (16/2), self.tank.facing, True))

            if self.enemies:
                for enemy in self.enemies:
                    enemy.update()
                    for bullet in self.bullets:
                        if not bullet.isAlive:
                            self.bullets.remove(bullet)
                        # print('working')
                        if enemy.x <= bullet.x <= enemy.x+16 and enemy.y <= bullet.y <= enemy.y+16 and bullet.isPlayer == True:
                            print('hit') 
                            self.enemies.remove(enemy)
                            self.bullets.remove(bullet)
                            self.blasts.append(Blast(enemy.x, enemy.y))

                        if self.tank.x < bullet.x < self.tank.x+16 and self.tank.y < bullet.y < self.tank.y+16:     
                            self.tank.isAlive = True
                            print('tank was hit')
                            self.bullets.remove(bullet) 
                             
                    willShoot = random.randint(0, BULLET_FREQUENCY)
                    # willShoot = 0
                    enemyBullet = Bullet(enemy.x + (16/2), enemy.y + (16/2), enemy.Dir, False)
                    if willShoot == 1:
                        self.bullets.append(enemyBullet)
                        

            if self.bullets:
                for bullet in self.bullets:
                    bullet.update()
            
            if self.blasts:
                for blast in self.blasts:
                    blast.update()
            
            for i in range(len(self.blasts)):
                if not self.blasts[i].isAlive:
                    del self.blasts[i]

                

    def draw(self):
        self.tank.draw()
        for enemy in self.enemies:
            enemy.draw()
        for bullet in self.bullets:
            bullet.draw()    
        for blast in self.blasts:
            blast.draw()

        pyxel.blt(16,16, 0, 0, 0, 16, 16)
        pyxel.blt(32,32, 0 , 16, 0, 16, 16)
        pyxel.blt(48, 48, 0, 0, 16, 16, 16)
        pyxel.blt(64,64, 0 ,0, 32, 16,16)
        

App()
import pyxel
import random
from tank import Tank
from enemy import Enemy
from bullet import Bullet

BULLET_FREQUENCY = 20
 
class App:
    def __init__(self):
        pyxel.init(320, 240)
        self.x = 0
        self.y = 0
        self.tank = Tank(self.x, self.y)
        self.enemies = []
        self.bullets = []
        
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
                        if not(0 <= bullet.x <= pyxel.width and 0 <= bullet.y <= pyxel.height):
                            self.bullets.remove(bullet)
                        # print('working')
                        if enemy.x <= bullet.x <= enemy.x+16 and enemy.y <= bullet.y <= enemy.y+16 and bullet.isPlayer == True:
                            print('hit') 
                            self.enemies.remove(enemy)
                            self.bullets.remove(bullet) 

                        if self.tank.x < bullet.x < self.tank.x+16 and self.tank.y < bullet.y < self.tank.y+16:     
                            self.tank.isAlive = False
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
                

    def draw(self):
        self.tank.draw()
        for enemy in self.enemies:
            enemy.draw()
        for bullet in self.bullets:
            bullet.draw()        
        

App()
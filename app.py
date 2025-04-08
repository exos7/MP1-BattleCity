import pyxel
from player import Player
from functions import boundingBox, inBounds, atTop, atBottom, atLeft, atRight, boundingBoxCollisionTop, \
boundingBoxCollisionBottom, boundingBoxCollisionLeft, boundingBoxCollisionRight, isColliding, boundingBoxCollision, boundingBoxCollisionBullet
from settings import moveSpeed, borderLeft, borderRight, borderTop, borderBot, tileSize, bulletSpeed, shootingFrequency
from blocks import Block, Brick, crackedBrick, Water, Forest, Stone, Home, Mirror, enemySpawn, Blast, Powerup, Shield, playerShield, Health
from bullets import Bullet
from enemy import Enemy, Blue, Red
import random
from tilemap import level_1, level_2, test
from level import Screen, nextLevel, Win, gameOver, Start

def entityDraw(entities):
    for entity in entities:
        entity.draw()

def entityUpdate(entities):
    for entity in entities:
        entity.update()

def levelDraw(level):
    for block in level:
        block.draw()

def forestDraw(level):
    for block in level:
        if block.type == 'forest':
            block.draw()

def tileParser(self, tilemap):
    for row in range(0, 17):
        for col in range(0, 17):
            tile = tilemap[row][col]
            # tile = level_2[row][col]
            #Note that row and col must be rearranged to correct for pyxel's coordinate system
            b = Block((col+1)*tileSize, (row+1)*tileSize)
            if tile == 'empty':
                pass
            elif tile == 'brick':
                self.level.append(Brick(b.x, b.y))

            elif tile == 'crackedBrick':
                self.level.append(crackedBrick(b.x, b.y))

            elif tile == 'stone':
                self.level.append(Stone(b.x, b.y))

            elif tile == 'water':
                self.level.append(Water(b.x, b.y))

            elif tile == 'forest':
                self.level.append(Forest(b.x, b.y))
            
            elif tile == 'home':
                self.level.append(Home(b.x, b.y))

            elif tile == 'mirrorPos':
                self.level.append(Mirror(b.x, b.y, 0))
            
            elif tile == 'mirrorNeg':
                self.level.append(Mirror(b.x, b.y, 1))
            
            elif tile == 'enemySpawn':
                self.level.append(enemySpawn(b.x, b.y))
                self.enemySpawn.append((b.x, b.y))
                
            elif tile == 'playerSpawn':
                self.startX, self.startYy = b.x, b.y

class App:
    def __init__(self):
        '''
        272 x 272 play area
        top left corner is 16, 16
        top right corner is 304, 16
        bottom right corner is 288, 288
        bottom left corner is 16, 288
        bottom middle is 152, 288
        '''

        pyxel.init(272 + borderLeft + borderRight, 272 + borderTop + borderBot) #17x17 tiles w/ border
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')

        self.startX, self.startY = ((pyxel.width - borderLeft - borderRight) // 2) - (3* tileSize) // 2, pyxel.height - borderBot - tileSize #in case spawn doesn't parse
        
        self.totalEnemies = []
        self.enemies = []
        self.enemyNum = 10 #num of enemies needed to be eliminated 
        self.done = False
        self.screen = []
        self.enemySpawn = []
        self.levelNum = 1
        self.level = []
        self.blasts = []
        self.levelPowerups = []
        self.start = False
        self.gatlingGun = False
        self.ghost = False

        tileParser(self, level_1)

        self.player = Player(self.startX, self.startY)    
                
        for i in range(self.enemyNum):
            spawn = random.randint(0, len(self.enemySpawn)-1)
            enemyType = random.randint(0,1)
            x, y = self.enemySpawn[spawn][0], self.enemySpawn[spawn][1]
            orientation = random.randint(0, 3)
            self.totalEnemies.append(Blue(x,y,orientation) if enemyType == 0 else Red(x,y,orientation))

        pyxel.run(self.update, self.draw)

    
    def update(self):

        #cheatcodes
        if pyxel.btn(pyxel.KEY_F) and pyxel.btn(pyxel.KEY_U) and pyxel.btn(pyxel.KEY_N):
            self.player.lives += 1
            pyxel.play(0, 5)

        if pyxel.btn(pyxel.KEY_C) and pyxel.btn(pyxel.KEY_S):
            self.player.shields.append(playerShield(self.player.x, self.player.y))
            self.player.isShielded = True
            pyxel.play(0, 3)
        
        if pyxel.btn(pyxel.KEY_G) and pyxel.btn(pyxel.KEY_A) and pyxel.btn(pyxel.KEY_B) and pyxel.btn(pyxel.KEY_E):
            self.gatlingGun = not self.gatlingGun
            pyxel.play(0, 3)

        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.ghost = not self.ghost
            pyxel.play(0, 3)
            



        if not self.start:
            pyxel.playm(0)
            self.start = True

        

        self.player.update()
        entityUpdate(self.player.bullets)
        entityUpdate(self.level)
        entityUpdate(self.blasts)


        for enemy in self.totalEnemies:
            if len(self.enemies) < 5 and self.totalEnemies:
                if not any([boundingBoxCollision(enemy, enemy2) for enemy2 in self.enemies]) and not boundingBoxCollision(self.player, enemy):
                    self.enemies.append(enemy)
                    self.totalEnemies.remove(enemy)
        
        
        if self.player.isShielded:
            for shields in self.player.shields:
                shields.update(self.player.x - 4, self.player.y - 4)

        for powerup in self.levelPowerups:
            if boundingBoxCollision(self.player, powerup):
                if powerup.type == 'shield':
                    pyxel.play(0, 3)
                    self.player.shields.append(playerShield(self.player.x, self.player.y))
                    self.player.isShielded = True
                    self.levelPowerups.remove(powerup)
                if powerup.type == 'health':
                    pyxel.play(0, 5)
                    self.player.lives += 1
                    self.levelPowerups.remove(powerup)

        # movement mechanics neon mains
        if inBounds(self.player.x, self.player.y) and self.player.isAlive and self.player.canMove: 
            click = False
            if pyxel.btn(pyxel.KEY_W) and not click:
                click = True
                self.player.facing = 0
                if (not atTop(self.player.x, self.player.y) and not any([boundingBoxCollisionBottom(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionBottom(self.player, enemy) for enemy in self.enemies])) or (self.ghost and not atTop(self.player.x, self.player.y)):
                    self.player.y -= moveSpeed
            if pyxel.btn(pyxel.KEY_D) and not click:
                click = True
                self.player.facing = 1
                if not atRight(self.player.x, self.player.y) and not any([boundingBoxCollisionLeft(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionLeft(self.player, enemy) for enemy in self.enemies]) or (self.ghost and not atRight(self.player.x, self.player.y)):
                    self.player.x += moveSpeed
            if pyxel.btn(pyxel.KEY_S) and not click:
                click = True
                self.player.facing = 2
                if not atBottom(self.player.x, self.player.y) and not any([boundingBoxCollisionTop(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionTop(self.player, enemy) for enemy in self.enemies]) or (self.ghost and not atBottom(self.player.x, self.player.y)):
                    self.player.y += moveSpeed
            if pyxel.btn(pyxel.KEY_A) and not click:
                click = True
                self.player.facing = 3
                if not atLeft(self.player.x, self.player.y) and not any([boundingBoxCollisionRight(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionRight(self.player, enemy) for enemy in self.enemies]) or (self.ghost and not atLeft(self.player.x, self.player.y)):
                    self.player.x -= moveSpeed

        # enemy movement
        for enemy in self.enemies:
            if pyxel.frame_count % 30 == 0:
                enemy.facing = random.randint(0, 3) 
            Dir = enemy.facing
            if inBounds(enemy.x, enemy.y):
                if Dir == 0 and not atTop(enemy.x, enemy.y) and not any([boundingBoxCollisionBottom(enemy, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not boundingBoxCollisionBottom(enemy, self.player) and not any([boundingBoxCollisionBottom(enemy, enemy2) for enemy2 in self.enemies if enemy2 != enemy]):
                    enemy.y -= moveSpeed
                    enemy.facing = 0
                if Dir == 1 and not atRight(enemy.x, enemy.y) and not any([boundingBoxCollisionLeft(enemy, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not boundingBoxCollisionLeft(enemy, self.player) and not any([boundingBoxCollisionLeft(enemy, enemy2) for enemy2 in self.enemies if enemy2 != enemy]):
                    enemy.x += moveSpeed
                    enemy.facing = 1
                if Dir == 2 and not atBottom(enemy.x, enemy.y) and not any([boundingBoxCollisionTop(enemy, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not boundingBoxCollisionTop(enemy, self.player) and not any([boundingBoxCollisionTop(enemy, enemy2) for enemy2 in self.enemies if enemy2 != enemy]):
                    enemy.y += moveSpeed
                    enemy.facing = 2
                if Dir == 3 and not atLeft(enemy.x, enemy.y) and not any([boundingBoxCollisionRight(enemy, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not boundingBoxCollisionRight(enemy, self.player) and not any([boundingBoxCollisionRight(enemy, enemy2) for enemy2 in self.enemies if enemy2 != enemy]):
                    enemy.x -= moveSpeed
                    enemy.facing = 3
            willshoot = random.randint(0, shootingFrequency)
            if willshoot == 1 and not enemy.isShooting:
                enemy.isShooting = True
                enemy.bullets.append(Bullet(enemy.x, enemy.y, enemy.facing))

            enemy.bullets = [bullet for bullet in enemy.bullets if inBounds(bullet.x, bullet.y)]
            if len(enemy.bullets) == 0:
                enemy.isShooting = False

            entityUpdate(enemy.bullets)
            for bullet in enemy.bullets:

                if self.player.isShielded:
                    for shield in self.player.shields:
                        if boundingBoxCollisionBullet(bullet, shield):
                            if bullet in enemy.bullets:
                                enemy.bullets.remove(bullet)
                            if shield in self.player.shields:
                                self.player.shields.remove(shield)
                            pyxel.play(0, 4)
                            # print('shield was hit')

                #logic for shooting player
                if boundingBoxCollisionTop(bullet, self.player) or boundingBoxCollisionBottom(bullet, self.player) or \
                        boundingBoxCollisionRight(bullet, self.player) or boundingBoxCollisionLeft(bullet, self.player):
                    enemy.isShooting = False
                    self.player.lives -= 1
                    if bullet in enemy.bullets:
                        pyxel.play(2, 2)
                        enemy.bullets.remove(bullet) 
                    # print('player was hit')
                    if self.player.lives <= 0:
                        self.player.isAlive = False
                        # print('player is dead and can no longer move')
                        self.totalEnemies.clear()
                        self.level.clear()
                        self.enemies.clear()
                        s = Screen(36+borderLeft, 36+borderTop)
                        self.screen.append(gameOver(s.x, s.y))


        
                        

                for block in self.level:
                    if block.type == 'brick':
                        if boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                        boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block):
                            enemy.isShooting = False
                            self.level.remove(block)
                            self.level.append(crackedBrick(block.x, block.y))
                                
                        
                    elif block.type == 'crackedBrick' or block.type == 'stone' or block.type == 'home':
                        if boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                            boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block):
                            if enemy.bullets: 
                                enemy.bullets.remove(bullet)
                            if block.type == 'crackedBrick':
                                block.health -= 10 
                                if block.health <= 0:
                                    self.level.remove(block)
                            elif block.type == 'home':
                                block.health -= 10
                                if block.health <= 0:
                                    # print('player is dead and can no longer move')
                                    self.level.clear()
                                    self.enemies.clear()
                                    s = Screen(36+borderLeft, 36+borderTop)
                                    self.screen.append(gameOver(s.x, s.y))
                                    self.player.isAlive = False
                    
                    elif block.type == 'mirror':
                        for i, pixels in enumerate(block.pixels):
                            if bullet.facing == 0: #shot beneath mirror
                                if bullet.x == pixels[0]:
                                    if block.orientation == 0:
                                        if block.pixels[i][1] - bulletSpeed  <= bullet.y <= block.pixels[i-1][1] + bulletSpeed and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 1
                                    elif block.orientation == 1:
                                        if block.pixels[i-1][1] - bulletSpeed <= bullet.y <= block.pixels[i][1] + bulletSpeed  and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 3
                            elif bullet.facing == 1:
                                if bullet.y == pixels[1]:
                                    if block.orientation == 0:
                                        if block.pixels[i-1][0] - bulletSpeed <= bullet.x <= block.pixels[i][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 0
                                    elif block.orientation == 1:
                                        if block.pixels[i][0] - bulletSpeed <= bullet.x <= block.pixels[i-1][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 2
                            elif bullet.facing == 2:
                                if bullet.x == pixels[0]:
                                    if block.orientation == 0:
                                        if block.pixels[i-1][1] - bulletSpeed <= bullet.y <= block.pixels[i][1] + bulletSpeed and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 3
                                    elif block.orientation == 1:
                                        if block.pixels[i][1] - bulletSpeed <= bullet.y <= block.pixels[i-1][1] + bulletSpeed and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 1
                            elif bullet.facing == 3:
                                if bullet.y == pixels[1]:
                                    if block.orientation == 0:
                                        if block.pixels[i][0] - bulletSpeed <= bullet.x <= block.pixels[i-1][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 2
                                    elif block.orientation == 1:
                                        if block.pixels[i-1][0] - bulletSpeed <= bullet.x <= block.pixels[i][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                            block.bulletsCollided.append(bullet)
                                            bullet.facing = 0
                    
                    
        
                    
                    if len(enemy.bullets) == 0:
                        enemy.isShooting = False


        # player shooting
        if not self.gatlingGun:
            if pyxel.btnp(pyxel.KEY_SPACE,15,20) and not self.player.isShooting and self.player.canMove:
                self.player.isShooting = True
                self.player.bullets.append(Bullet(self.player.x, self.player.y, self.player.facing))
                pyxel.play(3, 0)
        else:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.player.isShooting = True
                self.player.bullets.append(Bullet(self.player.x, self.player.y, self.player.facing))
                pyxel.play(3, 0) 

        self.player.bullets = [bullet for bullet in self.player.bullets if inBounds(bullet.x, bullet.y)]
        
        if len(self.player.bullets) == 0:
            self.player.isShooting = False

        for bullet in self.player.bullets:
            if boundingBoxCollision(bullet, self.player):
                if bullet in self.player.bullets:
                    pyxel.play(2, 2)
                    self.player.bullets.remove(bullet)
                    if any(boundingBoxCollision(bullet, shield) for shield in self.player.shields):
                        self.player.shields.pop(0)
                    self.player.lives -= 1
                if self.player.lives <= 0:
                    self.player.isAlive = False
                    # print('player is dead and can no longer move')
                    self.totalEnemies.clear()
                    self.level.clear()
                    self.enemies.clear()
                    s = Screen(36+borderLeft, 36+borderTop)
                    self.screen.append(gameOver(s.x, s.y))

            #logic for player shooting
            for enemy in self.enemies:
                if boundingBoxCollisionTop(bullet, enemy) or boundingBoxCollisionBottom(bullet, enemy) or \
                    boundingBoxCollisionRight(bullet, enemy) or boundingBoxCollisionLeft(bullet, enemy):
                    self.player.isShooting = False
                    enemy.health -= 10 
                    if enemy.health <= 0:
                        pyxel.play(2, 2)
                        self.blasts.append(Blast(enemy.x, enemy.y))
                        if self.player.killsForPowerups == 3:
                            randomPowerup = random.randint(0, 1)
                            if randomPowerup == 0:
                                self.levelPowerups.append(Shield(enemy.x, enemy.y))
                            elif randomPowerup == 1:
                                self.levelPowerups.append(Health(enemy.x, enemy.y))
                            self.player.killsForPowerups = 0
                        self.enemies.remove(enemy)
                        self.player.killsForPowerups += 1
                    elif enemy.type == 'red':
                        pyxel.play(0, 6)
                    if bullet in self.player.bullets:
                        self.player.bullets.remove(bullet)

                    if len(self.enemies) <= 0 and len(self.totalEnemies) <= 0:
                        # print('you won!')
                        #function for win screen! 
                        self.level.clear()
                        self.levelPowerups.clear()
                        self.levelNum += 1
                        s = Screen(36+borderLeft, 36+borderTop)
                        if self.levelNum <= 2:
                            self.screen.append(nextLevel(s.x, s.y))
                        else:
                            self.screen.append(Win(s.x, s.y))
                        self.player.canMove = False

                for enemyBullet in enemy.bullets:
                    if boundingBoxCollisionBullet(bullet, enemyBullet):
                        self.blasts.append(Blast(bullet.x-bulletSpeed, bullet.y+bulletSpeed))
                        if enemy.bullets:
                            enemy.bullets.remove(enemyBullet)
                        if bullet in self.player.bullets:
                            self.player.bullets.remove(bullet)
        
            

            
            for block in self.level:
                if block.type == 'crackedBrick' or block.type == 'brick' or block.type == 'stone' or block.type == 'home':
                    if boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                        boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block):
                        self.player.isShooting = False 
                        if block.type == 'crackedBrick' or block.type == 'brick':
                            block.health -= 10 
                            if block.health <= 0:
                                self.level.remove(block)
                        elif block.type == 'home':
                            block.health -= 10
                            if block.health <= 0:
                                # print('player is dead and can no longer move')
                                s = Screen(36+borderLeft, 36+borderTop)
                                self.screen.append(gameOver(s.x, s.y))
                                self.level.clear()
                                self.enemies.clear()
                                self.totalEnemies.clear()
                                self.levelPowerups.clear()
                                self.player.isAlive = False
                                #add game over screen
                        if bullet in self.player.bullets:
                            self.player.bullets.remove(bullet)
                
                elif block.type == 'mirror':
                    for i, pixels in enumerate(block.pixels):
                        if bullet.facing == 0: #shot beneath mirror
                            if bullet.x == pixels[0]:
                                if block.orientation == 0:
                                    if block.pixels[i][1] - bulletSpeed  <= bullet.y <= block.pixels[i-1][1] + bulletSpeed and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 1
                                elif block.orientation == 1:
                                    if block.pixels[i-1][1] - bulletSpeed <= bullet.y <= block.pixels[i][1] + bulletSpeed  and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 3
                        elif bullet.facing == 1:
                            if bullet.y == pixels[1]:
                                if block.orientation == 0:
                                    if block.pixels[i-1][0] - bulletSpeed <= bullet.x <= block.pixels[i][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 0
                                elif block.orientation == 1:
                                    if block.pixels[i][0] - bulletSpeed <= bullet.x <= block.pixels[i-1][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 2
                        elif bullet.facing == 2:
                            if bullet.x == pixels[0]:
                                if block.orientation == 0:
                                    if block.pixels[i-1][1] - bulletSpeed <= bullet.y <= block.pixels[i][1] + bulletSpeed and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 3
                                elif block.orientation == 1:
                                    if block.pixels[i][1] - bulletSpeed <= bullet.y <= block.pixels[i-1][1] + bulletSpeed and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 1
                        elif bullet.facing == 3:
                            if bullet.y == pixels[1]:
                                if block.orientation == 0:
                                    if block.pixels[i][0] - bulletSpeed <= bullet.x <= block.pixels[i-1][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 2
                                elif block.orientation == 1:
                                    if block.pixels[i-1][0] - bulletSpeed <= bullet.x <= block.pixels[i][0] + bulletSpeed and bullet not in block.bulletsCollided:
                                        block.bulletsCollided.append(bullet)
                                        bullet.facing = 0

        if (pyxel.btnp(pyxel.KEY_C) and self.player.canMove == False and self.levelNum == 2):
            self.level.clear()
            self.level2()

        if pyxel.btnp(pyxel.KEY_2):
            self.levelNum = 2
            self.level.clear()
            self.level2()
        elif pyxel.btnp(pyxel.KEY_C) and self.player.canMove == False and self.levelNum > 2:
            quit()

        elif (pyxel.btnp(pyxel.KEY_R) and self.player.canMove == False and self.levelNum > 2) or pyxel.btnp(pyxel.KEY_1):
            self.restart()

        elif pyxel.btnp(pyxel.KEY_C) and self.player.isAlive == False:
            self.restart()



    def restart(self):
        self.startX, self.startY = ((pyxel.width - borderLeft - borderRight) // 2) - (3* tileSize) // 2, pyxel.height - borderBot - tileSize
        self.player = Player(self.startX, self.startY)
        self.totalEnemies = []
        self.enemies = []
        self.enemyNum = 10 #num of enemies needed to be eliminated 
        self.done = False
        self.screen = []
        self.enemySpawn = []
        self.levelNum = 1
        self.level = []
        self.blasts = []
        self.levelPowerups = []
        self.start = False
        tileParser(self, level_1)
                    
        for i in range(self.enemyNum):
            spawn = random.randint(0, len(self.enemySpawn)-1)
            enemyType = random.randint(0,1)
            x, y = self.enemySpawn[spawn][0], self.enemySpawn[spawn][1]
            orientation = random.randint(0, 3)
            self.totalEnemies.append(Blue(x,y,orientation) if enemyType == 0 else Red(x,y,orientation))
    
    def level2(self):
        self.screen.clear()
        self.enemies.clear()
        self.player.facing = 0
        self.player.canMove = True
        self.totalEnemies = []
        self.enemySpawn = []
        self.enemyNum = 10
        self.screen = []
        self.levelPowerups = []
        self.player.x, self.player.y = self.startX, self.startY
        self.player.shields = []

        tileParser(self, level_2)

        for i in range(self.enemyNum):
            spawn = random.randint(0, len(self.enemySpawn)-1)
            enemyType = random.randint(0,1)
            x, y = self.enemySpawn[spawn][0], self.enemySpawn[spawn][1]
            orientation = random.randint(0, 3)
            self.totalEnemies.append(Blue(x,y,orientation) if enemyType == 0 else Red(x,y,orientation))
        pyxel.playm(0)

    def draw(self):
        if not self.done:

            self.player.draw()
            
            
            entityDraw(self.enemies)
            entityUpdate(self.enemies)
            entityDraw(self.blasts)
            entityDraw(self.levelPowerups)
            #left border
            pyxel.rect(0, 0, borderLeft, pyxel.height, 13)
            #right border
            pyxel.rect(pyxel.width - borderRight, 0, borderRight, pyxel.height, 13)
            #top border
            pyxel.rect(0, 0, pyxel.width, borderTop, 13)
            #bottom border
            pyxel.rect(0, pyxel.height - borderBot, pyxel.width, borderBot, 13)
            
            pyxel.blt(pyxel.width - borderRight + 8, pyxel.height - borderBot - 8, 2, 0, 32, 8, 8, 0)
            pyxel.text(pyxel.width - borderRight + 18, pyxel.height - borderBot - 6, f'{self.player.lives}', 0)

            for i in range(len(self.totalEnemies)):
                if i % 2 != 0:
                    pyxel.blt(pyxel.width - borderRight + 8, borderTop + 8*(i-1), 2, 0, 0, 8, 8)
                else:
                    pyxel.blt(pyxel.width - borderRight + 18 , borderTop + 8*(i), 2, 0, 0, 8, 8)

            levelDraw(self.level)
            entityDraw(self.player.bullets)
            entityDraw(self.screen)
            entityDraw(self.player.shields)
            for enemy in self.enemies:
                entityDraw(enemy.bullets)
                forestDraw(self.level)
        else:
            #consider making intial screen
            pass
        
App()
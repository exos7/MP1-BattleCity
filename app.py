from re import I
import pyxel
from player import Player
from functions import boundingBox, inBounds, atTop, atBottom, atLeft, atRight, boundingBoxCollisionTop, \
boundingBoxCollisionBottom, boundingBoxCollisionLeft, boundingBoxCollisionRight, isColliding, boundingBoxCollision
from settings import moveSpeed, borderLeft, borderRight, borderTop, borderBot, tileSize, bulletSpeed
from blocks import Block, Brick, crackedBrick, Water, Forest, Stone, Home, Mirror, enemySpawn
from bullets import Bullet
from enemy import Enemy, Blue, Red
import random
from tilemap import level_1, level_2
from level import Screen, nextLevel, Win, gameOver

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



        self.startX, self.startY = ((pyxel.width - borderLeft - borderRight) // 2) - (3* tileSize) // 2, pyxel.height - borderBot - tileSize
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        self.player = Player(self.startX, self.startY)
        self.totalEnemies = []
        self.enemies = []
        self.enemyNum = 10 #num of enemies needed to be eliminated 
        self.done = False
        self.screen = []
        self.enemySpawn = []
        self.levelNum = 1
        self.level = []
        
        for row in range(0, 17):
            for col in range(0, 17):
                tile = level_1[row][col]
                # tile = level_2[row][col]
                #Note that row and col must be rearranged to correct for pyxel's coordinate system
                b = Block((col+1)*tileSize, (row+1)*tileSize)
                if tile == 'empty':
                    pass
                elif tile == 'brick':
                    self.level.append(Brick(b.x, b.y))

                elif tile == 'cracked_brick':
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

        # adds the total enemies to a list
        for i in range(self.enemyNum):
            spawn = random.randint(0, len(self.enemySpawn)-1)
            enemyType = random.randint(0,1)
            x, y = self.enemySpawn[spawn][0], self.enemySpawn[spawn][1]
            self.totalEnemies.append(Blue(x,y) if enemyType == 0 else Red(x,y))


        pyxel.mouse(True)



        pyxel.run(self.update, self.draw)

        
    def update(self):
        self.player.update()
        entityUpdate(self.player.bullets)
        entityUpdate(self.level)

        for enemy in self.totalEnemies:
            if len(self.enemies) <= 5:
                if not any([boundingBoxCollision(enemy, enemy2) for enemy2 in self.enemies]):
                    self.enemies.append(enemy)
                    self.totalEnemies.remove(enemy)
                    

        # movement mechanics neon mains
        if inBounds(self.player.x, self.player.y) and self.player.isAlive and self.player.canMove: 
            click = False
            if pyxel.btn(pyxel.KEY_W) and not click:
                click = True
                self.player.facing = 0
                if not atTop(self.player.x, self.player.y) and not any([boundingBoxCollisionBottom(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionBottom(self.player, enemy) for enemy in self.enemies]):
                    self.player.y -= moveSpeed
            if pyxel.btn(pyxel.KEY_D) and not click:
                click = True
                self.player.facing = 1
                if not atRight(self.player.x, self.player.y) and not any([boundingBoxCollisionLeft(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionLeft(self.player, enemy) for enemy in self.enemies]):
                    self.player.x += moveSpeed
            if pyxel.btn(pyxel.KEY_S) and not click:
                click = True
                self.player.facing = 2
                if not atBottom(self.player.x, self.player.y) and not any([boundingBoxCollisionTop(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionTop(self.player, enemy) for enemy in self.enemies]):
                    self.player.y += moveSpeed
            if pyxel.btn(pyxel.KEY_A) and not click:
                click = True
                self.player.facing = 3
                if not atLeft(self.player.x, self.player.y) and not any([boundingBoxCollisionRight(self.player, block) for block in self.level if block.type not in ('forest', 'enemySpawn')]) and not any([boundingBoxCollisionRight(self.player, enemy) for enemy in self.enemies]):
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
            willshoot = random.randint(0, 50)
            if willshoot == 1 and not enemy.isShooting:
                enemy.isShooting = True
                enemy.bullets.append(Bullet(enemy.x, enemy.y, enemy.facing))

            enemy.bullets = [bullet for bullet in enemy.bullets if inBounds(bullet.x, bullet.y)]
            if len(enemy.bullets) == 0:
                enemy.isShooting = False

            entityUpdate(enemy.bullets)
            for bullet in enemy.bullets:

                #logic for shooting player
                if boundingBoxCollisionTop(bullet, self.player) or boundingBoxCollisionBottom(bullet, self.player) or \
                        boundingBoxCollisionRight(bullet, self.player) or boundingBoxCollisionLeft(bullet, self.player):
                    enemy.isShooting = False
                    self.player.lives -= 1
                    enemy.bullets.remove(bullet)
                    print('player was hit')
                    if self.player.life <= 0:
                        self.player.isAlive = False
                        print('player is dead and can no longer move')
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
                                
                        
                    elif block.type == 'cracked_brick' or block.type == 'stone' or block.type == 'home':
                        if boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                            boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block):
                            enemy.bullets.remove(bullet)
                            if block.type == 'cracked_brick':
                                block.health -= 10 
                                if block.health <= 0:
                                    self.level.remove(block)
                            elif block.type == 'home':
                                block.health -= 10
                                if block.health <= 0:
                                    print('player is dead and can no longer move')
                                    self.level.clear()
                                    self.enemies.clear()
                                    s = Screen(36+borderLeft, 36+borderTop)
                                    self.screen.append(gameOver(s.x, s.y))
                                    self.player.isAlive = False
                                    #add game over screen
                                    #funtionify initialization HASHFHADJKFALDSJHF
                    
                    if len(enemy.bullets) == 0:
                        enemy.isShooting = False


        # player shooting
        if pyxel.btnp(pyxel.KEY_SPACE,15,20) and not self.player.isShooting and self.player.canMove:
            self.player.isShooting = True
            self.player.bullets.append(Bullet(self.player.x, self.player.y, self.player.facing))


        # bullet collision 
        self.player.bullets = [bullet for bullet in self.player.bullets if inBounds(bullet.x, bullet.y)]
        
        if len(self.player.bullets) == 0:
            self.player.isShooting = False
        
        for bullet in self.player.bullets:

            #logic for shooting enemy
            for enemy in self.enemies:
                if boundingBoxCollisionTop(bullet, enemy) or boundingBoxCollisionBottom(bullet, enemy) or \
                    boundingBoxCollisionRight(bullet, enemy) or boundingBoxCollisionLeft(bullet, enemy):
                    self.player.isShooting = False
                    self.enemies.remove(enemy)
                    self.player.bullets.remove(bullet)
                    if self.enemyNum >= 0:
                        self.enemyNum -= 1
                        self.enemies.append(Blue(16, 16))
                    else:
                        print('you won!')
                        #function for win screen! 
                        self.level.clear()
                        self.levelNum += 1
                        s = Screen(36+borderLeft, 36+borderTop)
                        if self.levelNum <= 2:
                            self.screen.append(nextLevel(s.x, s.y))
                        else:
                            self.screen.append(Win(s.x, s.y))
                        self.player.canMove = False
                        #turn this into a function ? 
        

                        

            for block in self.level:
                if block.type == 'brick':
                    if boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                    boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block):
                        # self.player.bullets.remove(bullet)
                        self.player.isShooting = False 
                        if block.type == 'brick':
                            self.level.remove(block)
                            self.level.append(crackedBrick(block.x, block.y))
                            
                       
                elif block.type == 'cracked_brick' or block.type == 'stone' or block.type == 'home':
                    if boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                        boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block):
                        self.player.isShooting = False 
                        if block.type == 'cracked_brick':
                            block.health -= 10 
                            if block.health <= 0:
                                self.level.remove(block)
                        elif block.type == 'home':
                            block.health -= 10
                            if block.health <= 0:
                                print('player is dead and can no longer move')
                                s = Screen(36+borderLeft, 36+borderTop)
                                self.screen.append(gameOver(s.x, s.y))
                                self.level.clear()
                                self.enemies.clear()
                                self.player.isAlive = False
                                #add game over screen
                        if self.player.bullets:
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
                        
                # elif block.type == 'mirror':
                #     if (boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                #         boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block)) and pyxel.frame_count % 2 == 0:
                #         if block.orientation == 0:
                #             if bullet.facing == 0:
                #                 bullet.facing = 1
                #             elif bullet.facing == 1:
                #                 bullet.facing = 0
                #             elif bullet.facing == 2:
                #                 bullet.facing = 3
                #             elif bullet.facing == 3:
                #                 bullet.facing = 2
                                
                #         if block.orientation == 1:
                #             if bullet.facing == 0:
                #                 bullet.facing = 3
                #             elif bullet.facing == 1:
                #                 bullet.facing = 2
                #             elif bullet.facing == 2:
                #                 bullet.facing = 1
                #             elif bullet.facing == 3:
                #                 bullet.facing = 0


        if pyxel.btnp(pyxel.KEY_SPACE) and self.player.canMove == False and self.levelNum == 2:
            self.player.facing = 0
            self.player.canMove = True
            self.enemies = [Blue(16, 16)]
            self.enemyNum = 1
            self.screen = []
            self.player.x, self.player.y = self.startX, self.startY
            for row in range(0, 17):
                for col in range(0, 17):
                    # tile = level_1[row][col]
                    tile = level_2[row][col]
                    #Note that row and col must be rearranged to correct for pyxel's coordinate system
                    b = Block((col+1)*tileSize, (row+1)*tileSize)
                    if tile == 'empty':
                        pass
                    elif tile == 'brick':
                        print(f'brick: {b.x}, {b.y}')
                        self.level.append(Brick(b.x, b.y))

                    elif tile == 'cracked_brick':
                        print(f'cracked_brick: {b.x}, {b.y}')
                        self.level.append(crackedBrick(b.x, b.y))

                    elif tile == 'stone':
                        print(f'stone: {b.x}, {b.y}')
                        self.level.append(Stone(b.x, b.y))

                    elif tile == 'water':
                        print(f'water: {b.x}, {b.y}')
                        self.level.append(Water(b.x, b.y))

                    elif tile == 'forest':
                        print(f'forest: {b.x}, {b.y}')
                        self.level.append(Forest(b.x, b.y))
                    
                    elif tile == 'home':
                        print(f'brick: {b.x}, {b.y}')
                        self.level.append(Home(b.x, b.y))

                    elif tile == 'mirrorPos':
                        print(f'mirrorPos: {b.x}, {b.y}')
                        self.level.append(Mirror(b.x, b.y, 0))
                    
                    elif tile == 'mirrorNeg':
                        print(f'mirrorNeg: {b.x}, {b.y}')
                        self.level.append(Mirror(b.x, b.y, 1))

        elif pyxel.btnp(pyxel.KEY_SPACE) and self.player.canMove == False and self.levelNum > 2:
            #consider making initial screen
            quit()

        elif pyxel.btnp(pyxel.KEY_SPACE) and self.player.isAlive == False:
            quit() 

        
    def draw(self):
        if not self.done:

            self.player.draw()
            
            
                
            entityDraw(self.enemies)
            entityUpdate(self.enemies)
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
            pyxel.blt(pyxel.width - borderRight + 8, borderTop, 2, 0, 0, 8, 8)
            levelDraw(self.level)
            entityDraw(self.player.bullets)
            entityDraw(self.screen)
            for enemy in self.enemies:
                entityDraw(enemy.bullets)
                forestDraw(self.level)
        else:
            #consider making intial screen
            pass
        
App()
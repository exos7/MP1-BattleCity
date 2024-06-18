from re import I
import pyxel
from player import Player
from functions import boundingBox, inBounds, atTop, atBottom, atLeft, atRight, boundingBoxCollisionTop, \
boundingBoxCollisionBottom, boundingBoxCollisionLeft, boundingBoxCollisionRight
from settings import moveSpeed, borderLeft, borderRight, borderTop, borderBot, tileSize
from blocks import Block, Brick, Water, Leaves, Unbreakable
from bullets import Bullet


def entityDraw(entities):
    for entity in entities:
        entity.draw()

def entityUpdate(entities):
    for entity in entities:
        entity.update()

def levelDraw(level):
    for block in level:
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



        self.startX, self.startY = ((pyxel.width - borderLeft - borderRight) // 2) + tileSize // 2, pyxel.height - borderBot - tileSize 
        pyxel.load('PYXEL_RESOURCE_FILE.pyxres')
        self.player = Player(self.startX, self.startY)
        self.level = [Brick(tileSize * 12, tileSize*4), Unbreakable(tileSize * 13, tileSize*4), Brick(tileSize*14, tileSize*4)]

        pyxel.mouse(True)



        pyxel.run(self.update, self.draw)

        
    def update(self):
        self.player.update()
        entityUpdate(self.player.bullets)
        entityUpdate(self.level)

        if inBounds(self.player.x, self.player.y): # movement logic
            click = False
            if pyxel.btn(pyxel.KEY_W) and not click:
                click = True
                self.player.facing = 0
                if not atTop(self.player.x, self.player.y) and not any([boundingBoxCollisionBottom(self.player, block) for block in self.level]):
                    self.player.y -= moveSpeed
            if pyxel.btn(pyxel.KEY_D) and not click:
                click = True
                self.player.facing = 1
                if not atRight(self.player.x, self.player.y) and not any([boundingBoxCollisionLeft(self.player, block) for block in self.level]):
                    self.player.x += moveSpeed
            if pyxel.btn(pyxel.KEY_S) and not click:
                click = True
                self.player.facing = 2
                if not atBottom(self.player.x, self.player.y) and not any([boundingBoxCollisionTop(self.player, block) for block in self.level]):
                    self.player.y += moveSpeed
            if pyxel.btn(pyxel.KEY_A) and not click:
                click = True
                self.player.facing = 3
                if not atLeft(self.player.x, self.player.y) and not any([boundingBoxCollisionRight(self.player, block) for block in self.level]):
                    self.player.x -= moveSpeed

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.player.bullets.append(Bullet(self.player.x, self.player.y, self.player.facing))

        self.player.bullets = [bullet for bullet in self.player.bullets if inBounds(bullet.x, bullet.y)]
        
        for bullet in self.player.bullets:
            for block in self.level:
                if boundingBoxCollisionTop(bullet, block) or boundingBoxCollisionBottom(bullet, block) or \
                boundingBoxCollisionRight(bullet, block) or boundingBoxCollisionLeft(bullet, block):
                    self.player.bullets.remove(bullet) 
                    if block.type == 'brick':
                        block.health -= 10
                        if block.health <= 0:
                            self.level.remove(block)

        
        


        

    def draw(self):
        
        self.player.draw()
        #left border
        pyxel.rect(0, 0, borderLeft, pyxel.height, 13)
        #right border
        pyxel.rect(pyxel.width - borderRight, 0, borderRight, pyxel.height, 13)
        #top border
        pyxel.rect(0, 0, pyxel.width, borderTop, 13)
        #bottom border
        pyxel.rect(0, pyxel.height - borderBot, pyxel.width, borderBot, 13)

        levelDraw(self.level)
        entityDraw(self.player.bullets)
App()
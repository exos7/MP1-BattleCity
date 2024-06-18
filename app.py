import pyxel
from player import Player
from functions import inBounds, atTop, atBottom, atLeft, atRight, boundingBoxCollisionTop, \
boundingBoxCollisionBottom, boundingBoxCollisionLeft, boundingBoxCollisionRight
from settings import MoveSpeed, borderLeft, borderRight, borderTop, borderBot, tileSize
from blocks import Block, Brick, Water, Leaves, Unbreakable


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
        self.brick = Brick(48, 176)


        pyxel.mouse(True)



        pyxel.run(self.update, self.draw)

        
    def update(self):
        print(boundingBoxCollisionTop(self.player, self.brick))
        self.player.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if inBounds(self.player.x, self.player.y):
            click = False
            if pyxel.btn(pyxel.KEY_W) and not click:
                click = True
                self.player.facing = 0
                if not atTop(self.player.x, self.player.y) and not boundingBoxCollisionBottom(self.player, self.brick):
                    self.player.y -= MoveSpeed
            if pyxel.btn(pyxel.KEY_D) and not click:
                click = True
                self.player.facing = 1
                if not atRight(self.player.x, self.player.y) and not boundingBoxCollisionLeft(self.player, self.brick):
                    self.player.x += MoveSpeed
            if pyxel.btn(pyxel.KEY_S) and not click:
                click = True
                self.player.facing = 2
                if not atBottom(self.player.x, self.player.y) and not boundingBoxCollisionTop(self.player, self.brick):
                    self.player.y += MoveSpeed
            if pyxel.btn(pyxel.KEY_A) and not click:
                click = True
                self.player.facing = 3
                if not atLeft(self.player.x, self.player.y) and not boundingBoxCollisionRight(self.player, self.brick):
                    self.player.x -= MoveSpeed

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

        self.brick.draw()
App()
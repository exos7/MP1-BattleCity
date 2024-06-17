import pyxel
from player import Player
from functions import inBounds, atTop, atBottom, atLeft, atRight
from settings import MoveSpeed, borderLeft, borderRight, borderTop, borderBot, tileSize



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
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
    
    def update(self):

        '''
        left = True
        for enemies in range(10):
            while len(enemies) < 5:
                if left:
                    enemies.append(Enemy(left_x, y))
                else:
                    enemies.append(Enemy(right_x, y))
        '''
        self.player.update()
        print(self.player.x, self.player.y)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if inBounds(self.player.x, self.player.y):
            click = False
            if pyxel.btn(pyxel.KEY_W) and not atTop(self.player.x, self.player.y) and not click:
                self.player.y -= MoveSpeed
                click = True
                self.player.facing = 0
            if pyxel.btn(pyxel.KEY_D) and not atRight(self.player.x, self.player.y) and not click:
                self.player.x += MoveSpeed
                click = True
                self.player.facing = 1
            if pyxel.btn(pyxel.KEY_S) and not atBottom(self.player.x, self.player.y) and not click:
                self.player.y += MoveSpeed
                click = True
                self.player.facing = 2
            if pyxel.btn(pyxel.KEY_A) and not atLeft(self.player.x, self.player.y) and not click:
                self.player.x -= MoveSpeed
                click = True
                self.player.facing = 3

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

App()
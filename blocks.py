import pyxel
from functions import boundingBox

class Block:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
    
    def update(self):
        pass
    def draw(self):
        pass

class Brick(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 20
        self.type = 'brick'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, self.height, self.width)

class crackedBrick(Block):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 20
        self.type = 'cracked_brick'

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 16, self.height, self.width)

class Water(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'water'

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32, self.height, self.width)

class Forest(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'forest'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.height, self.width, 0)

class Stone(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'stone'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.height, self.width)

class Home(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 20
        self.type = 'home'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 48, self.height, self.width, 0)
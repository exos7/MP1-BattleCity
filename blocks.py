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
        self.health = 100
        self.type = 'brick'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, self.height, self.width)

class Water(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'water'

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32, self.height, self.width)

class Leaves(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'leaves'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.height, self.width)

class Unbreakable(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'unbreakable'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.height, self.width)
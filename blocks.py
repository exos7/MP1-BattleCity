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
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16)

class Water(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def update(self):
        pass

    def draw(self):
        pass

class Leaves(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def update(self):
        pass

    def draw(self):
        pass

class Unbreakable(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def update(self):
        pass

    def draw(self):
        pass
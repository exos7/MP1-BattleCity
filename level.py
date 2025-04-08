import pyxel

class Screen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pyxel.rect(self.x, self.y, 200, 150, 13)

class Start(Screen):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self):
        super().draw()
        pyxel.text(self.x + 32, self.y*2, "Press C to start!", 0)

class nextLevel(Screen):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self):
        super().draw()
        pyxel.text(self.x + 28, self.y*2, "Congratulations! Press C to continue!", 0)

class Win(Screen):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self):
        super().draw()
        pyxel.text(self.x + 32, self.y*2, "Congratulations! Press C to quit!", 0)
        pyxel.text(self.x + 32, self.y*2 + 10, "Press R to Restart!", 0)

class gameOver(Screen):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self):
        super().draw()
        pyxel.text(self.x + 32, self.y*2, "Game Over! Press C to try again!", 0)

class enemyUI:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    




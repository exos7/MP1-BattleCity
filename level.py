import pyxel

class Screen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass


    def draw(self):
        pyxel.rect(self.x, self.y, 200, 150, 13)

class nextLevel(Screen):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self):
        super().draw()
        pyxel.text(self.x, self.y*2, "Congratulations! Press SPACE to go to the next level!", 0)

class Win(Screen):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self):
        super().draw()
        pyxel.text(self.x, self.y*2, "Congratulations!", 0)

class gameOver(Screen):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self):
        super().draw()
        pyxel.text(self.x, self.y*2, "Game Over!", 0)




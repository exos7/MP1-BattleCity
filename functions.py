import pyxel

def atRight(x, y):
    if pyxel.width - 16 == x:
        return True

def atLeft(x, y):
    if 0 == x:
        return True

def atTop(x, y):
    if 0 == y:
        return True

def atBottom(x, y):
    if pyxel.height - 16 == y:
        return True
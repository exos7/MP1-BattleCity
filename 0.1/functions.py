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

def in_bounds(x, y):
    if 0 <= x <= pyxel.width and 0 <= y <= pyxel.height:
        return True

def is_colliding(entity1, entity2):
    if (entity1.x <= entity2.x <= entity1.x+16) and (entity1.y <= entity2.y <= entity1.y + 16):
        return True
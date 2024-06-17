import pyxel
from settings import borderLeft, borderRight, borderTop, borderBot, MoveSpeed

def atRight(x, y):
    if pyxel.width - borderRight - 16 == x:
        return True

def atLeft(x, y):
    if borderLeft == x:
        return True

def atTop(x, y):
    if borderTop == y:
        return True

def atBottom(x, y):
    if pyxel.height - borderBot - 16 == y:
        return True

def inBounds(x, y):
    if borderLeft <= x <= pyxel.width - borderRight and borderTop <= y <= pyxel.height - borderBot - borderTop:
        return True

def is_colliding(entity1, entity2):
    if (entity1.x <= entity2.x <= entity1.x+16) and (entity1.y <= entity2.y <= entity1.y + 16):
        return True

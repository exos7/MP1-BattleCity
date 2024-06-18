import pyxel
from settings import borderLeft, borderRight, borderTop, borderBot, MoveSpeed
from player import Player

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

def isColliding(entity1, entity2):
    if (entity1.x <= entity2.x <= entity1.x+16) and (entity1.y <= entity2.y <= entity1.y + 16):
        return True

def boundingBox(entity):
    return (entity.x, entity.y, entity.x + entity.width, entity.y + entity.height)

def boundingBoxCollisionTop(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if type(entity1) is Player:
        if (x1 < x4 and x2 > x3) and (y1 < y4 and (y2 + MoveSpeed) > y3):
            return True

def boundingBoxCollisionBottom(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if (x1 < x4 and x2 > x3) and (y1 - MoveSpeed < y4 and y2 > y3):
        return True

def boundingBoxCollisionLeft(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if (x1 < x4 and x2 + MoveSpeed > x3) and (y1 < y4 and y2 > y3):
        return True

def boundingBoxCollisionRight(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if (x1 - MoveSpeed < x4 and x2 > x3) and (y1 < y4 and y2 > y3):
        return True
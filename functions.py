import pyxel
from settings import borderLeft, borderRight, borderTop, borderBot, moveSpeed, offset

def atRight(x, y):
    if pyxel.width - borderRight - 16 == x:
        return True
    

def atLeft(x, y):
    if borderLeft == x:
        return True
    return False

def atTop(x, y):
    if borderTop == y:
        return True
    return False

def atBottom(x, y):
    if pyxel.height - borderBot - 16 == y:
        return True
    return False

def inBounds(x, y):
    if borderLeft <= x <= pyxel.width - borderRight and borderTop <= y <= pyxel.height - borderBot:
        return True
    return False

def isColliding(entity1, entity2):
    if (entity1.x <= entity2.x <= entity1.x+4) and (entity1.y <= entity2.y <= entity1.y + 4):
        return True

    return False

def boundingBox(entity):
    if entity.width == 1 and entity.height == 1:
        return (entity.x, entity.y, entity.x, entity.y)
    return (entity.x, entity.y, entity.x + entity.width, entity.y + entity.height)

def boundingBoxCollisionTop(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if (x1 < x4 and x2 > x3) and (y1 < y4 and (y2 + moveSpeed) > y3):
        return True
    return False

def boundingBoxCollisionBottom(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if (x1 < x4 and x2 > x3) and (y1 - moveSpeed < y4 and y2 > y3):
        return True
    return False
    
def boundingBoxCollisionLeft(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if (x1 < x4 and x2 + moveSpeed > x3) and (y1 < y4 and y2 > y3):
        return True
    return False

def boundingBoxCollisionRight(entity1, entity2):
    x1, y1, x2, y2 = boundingBox(entity1)
    x3, y3, x4, y4 = boundingBox(entity2)
    if (x1 - moveSpeed < x4 and x2 > x3) and (y1 < y4 and y2 > y3):
        return True
    return False


# def boundingBoxCollisionTopMirror(entity1, entity2):
#     x1, y1 = entity1.x, entity1.y
#     x3, y3, x4, y4 = boundingBox(entity2)
#     if (x1 < x4 and x2 > x3) and (y1 < y4 and (y2 + moveSpeed) > y3):
#         return True
#     return False

# def boundingBoxCollisionBottomMirror(entity1, entity2):
#     x1, y1 = entity1.x, entity1.y
#     x3, y3, x4, y4 = boundingBox(entity2)
#     if (x1 < x4 and x2 > x3) and (y1 - moveSpeed < y4 and y2 > y3):
#         return True
#     return False
    
# def boundingBoxCollisionLeftMirror(entity1, entity2):
#     x1, y1 = entity1.x, entity1.y
#     x3, y3, x4, y4 = boundingBox(entity2)
#     if (x1 < x4 and x2 + moveSpeed > x3) and (y1 < y4 and y2 > y3):
#         return True
#     return False

# def boundingBoxCollisionRightMirror(entity1, entity2):
#     x1, y1 = entity1.x, entity1.y
#     x3, y3, x4, y4 = boundingBox(entity2)
#     if (x1 - moveSpeed < x4 and x2 > x3) and (y1 < y4 and y2 > y3):
#         return True
#     return False
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
    if (entity1.x <= entity2.x <= entity1.x+16) and (entity1.y <= entity2.y <= entity1.y + 16):
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

def isSeparated(entity1, entity2):
    def getAxes(entity):
        axes = []
        x1, y1, x2, y2 = boundingBox(entity)
        axes.append((x2 - x1, y2 - y1))
        axes.append((y2 - y1, x1 - x2))
        return axes

    def project(entity, axis):
        x1, y1, x2, y2 = boundingBox(entity)
        points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        min_proj = max_proj = axis[0] * points[0][0] + axis[1] * points[0][1]
        for point in points[1:]:
            proj = axis[0] * point[0] + axis[1] * point[1]
            if proj < min_proj:
                min_proj = proj
            elif proj > max_proj:
                max_proj = proj
        return min_proj, max_proj

    axes1 = getAxes(entity1)
    axes2 = getAxes(entity2)

    for axis in axes1 + axes2:
        min_proj1, max_proj1 = project(entity1, axis)
        min_proj2, max_proj2 = project(entity2, axis)
        if max_proj1 < min_proj2 or max_proj2 < min_proj1:
            return True

    return False
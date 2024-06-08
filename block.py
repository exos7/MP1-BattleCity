import pyxel

#types: BRICK, STONE, HORI_HALF_BRICK, HORI_HALF_STONE, WATER, ETC.
SIZE = 16

class Block:
    def __init__(self, coords):
        self.x, self.y, self.type = coords.x, coords.y, coords.type

    def update(self):
        pass

    def draw(self):
        if self.type == 'BRICK':
            pyxel.blt(self.x, self.y, 0, 0, 16, 16, SIZE)
            # print('brick')

        elif self.type == 'STONE':
            pyxel.blt(self.x, self.y, 0, 0, 0 ,16, SIZE)

        elif self.type == 'HORI_HALF_BRICK':
            pyxel.blt(self.x, self.y, 0, 0, 16, 16, SIZE/2)

        elif self.type == 'HORI_HALF_STONE':
            pyxel.blt(self.x, self.y, 0, 0, 0, 16, SIZE/2)
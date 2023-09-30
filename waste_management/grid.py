import enum

from .entity import Entity


class TileCharacteristic(enum.Enum):
    KEY = 0
    EXIT = 1
    FOOD = 2
    GLASS = 3
    DEATH = 4
    PLAGUE = 5
    SLICK = 6
    NORMAL = 10


class Tile(Entity): pass


class Grid(Entity):
    def new(self):
        self._tiles = []
        for x in range(self.x):
            self._tiles.append([])
            for y in range(self.y):
                self._tiles[x].append(
                    Tile(10, 10, self.scale)
                )


    def draw(self, canvas):
        for x in self._tiles:
            for y in x:
                y.draw(canvas)

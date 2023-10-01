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
    def setup(self, grid_width, grid_height):
        self._grid_width = grid_width
        self._grid_height = grid_height
        self._tiles = []

        for x in range(0, self._grid_width):
            self._tiles.append([])
            for y in range(0, self._grid_height):
                self._tiles[x].append(
                    Tile(25*x, 25*y, 20, 20, self.scale)
                )


    def draw(self, canvas):
        for x in self._tiles:
            for y in x:
                y.draw(canvas)

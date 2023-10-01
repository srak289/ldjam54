import dataclasses
import enum.Enum
import random

from .entity import Entity
from .event import TILE_SHUF_ATTR


class TileCharacteristic(enum.Enum):
    KEY = 0
    EXIT = 1
    FOOD = 2
    GLASS = 3
    DEATH = 4
    PLAGUE = 5
    SLICK = 6
    NORMAL = 10


class TileBufWeights: pass


@dataclasses.dataclass(freeze=True)
class TileColor:
    PLAYER = (66, 135, 245)
    KEY = (197, 207, 60)
    EXIT = (135, 214, 177)
    FOOD = (77, 171, 56)
    GLASS = (252, 169, 114)
    DEATH = (99, 24, 24)
    PLAGUE = (191, 152, 44)
    SLICK = (64, 53, 89)
    NORMAL = (175, 181, 189)


class Tile(Entity):
    special: bool = False
    sbuf: typing.Set = dataclasses.field(default_factory=lambda: set())
    buf: typing.Set = dataclasses.field(default_factory=lambda: set())

    def _attr_shuf(self):
        cur = self.buf
        self.buf = set()

    def setup(self):
        pass

    def dispatch(self, event):
        if event == TILE_SHUF_ATTR:
            self._attr_shuffle()
        elif event == pygame.



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

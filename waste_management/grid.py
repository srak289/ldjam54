import dataclasses
import random

from .entity import Entity
from .event import TILE_SHUF_ATTR
from .tile import Tile


@dataclasses.dataclass
class Grid(Entity):
    grid_width: int = 10
    grid_height: int = 10
    tiles: list = dataclasses.field(default_factory=lambda: list())
    num_keys: int = 5


    def set_size(self, width, height):
        self.grid_width = width
        self.grid_height = height

    def setup(self):
        for x in range(0, self.grid_width):
            self.tiles.append([])
            for y in range(0, self.grid_height):
                self.tiles[x].append(
                    Tile(25*x, 25*y, 20, 20, self.scale)
                )
        self._choose_key()
        self._choose_glass()
        self._choose_exit()


    def _choose_key(self):
        for _ in range(0, self.num_keys):
            x = random.choice(range(0, self.grid_width))
            y = random.choice(range(0, self.grid_height))
            self.tiles[x][y].add_schar(TileCharacteristic.KEY)


    def _choose_glass(self):
        for y in range(0, self.grid_height):
            x = random.choice(range(0, self.grid_width))
            self.tiles[x][y].add_schar(TileCharacteristic.GLASS)


    def _choose_exit(self):
        x = random.choice(range(0, self.grid_width))
        y = random.choice(range(0, self.grid_height))
        self.tiles[x][y].add_schar(TileCharacteristic.EXIT)


    def draw(self, canvas):
        for x in self.tiles:
            for y in x:
                y.draw(canvas)

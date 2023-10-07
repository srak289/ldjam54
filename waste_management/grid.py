import dataclasses
import random

from .entity import Entity
from .event import TILE_SHUF_ATTR
from .tile import Tile
from .tilemeta import *


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
        for y in range(0, self.grid_height):
            self.tiles.append([])
            for x in range(0, self.grid_width):
                self.tiles[y].append(
                    Tile(25*x, 25*y, 20, 20, self.scale)
                )
        self._select_exit()
        self._select_keys()
        self._select_glass()


    def _select_exit(self):
        y = random.choice(range(0, self.grid_height))
        x = random.choice(range(0, self.grid_width))
        self.tiles[y][x].add_attr(ExitTile)


    def _select_keys(self):
        for _ in range(0, self.num_keys):
            # we should ensure that the key does not
            # land on the exit
            y = random.choice(range(0, self.grid_height))
            x = random.choice(range(0, self.grid_width))
            self.tiles[y][x].add_attr(KeyTile)


    def _select_glass(self):
        for y in range(0, self.grid_height):

            # this could loop for "harder" levels
            # where there could be more than one glass tile per row
            # for _ in range(0, self.num_glass):
            # we would need to ensure the tiles selected were not special
            # x = random.choice(range(0, self.grid_width))
            # if self.tiles[x][y].is_special: ...
            
            x = random.choice(range(0, self.grid_width))
            self.tiles[y][x].add_attr(GlassTile)


    def dispatch(self, event):
        if event == GRID_COLLAPSE:
            pass
            # for y in 
            #   for x in
            #       self.tiles[y].remove(self.tiles[y][x]
            # after current glass tiles collapse
            # we select new ones with the same function
            self._select_glass()


    def draw(self, canvas):
        for y in self.tiles:
            for x in y:
                x.draw(canvas)

import dataclasses
import random

from .entity import Entity
from .event import *
from .tile import Tile
from .tilemeta import *


@dataclasses.dataclass
class Grid(Entity):
    grid_width: int = 20
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
                # TODO `35` should not be static
                self.tiles[y].append(
                    Tile(35*x, 35*y, 30, 30, self.scale)
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

    def _set_tile_position(self):
        for i, y in enumerate(self.tiles):
            for j, x in enumerate(y):
                # TODO this should account for scale
                # TODO `35` should not be static
                x.set_position(35*j, 35*i)

    def dispatch(self, event):
        if event == GRID_COLLAPSE:
            for y in self.tiles:
                r = []
                for x in y:
                    if GlassTile in x.buf:
                        r.append(x)
                for z in r:
                    y.remove(z)

            self.grid_width -= 1
            self._set_tile_position()
            self._select_glass()
        else:
            # TODO
            # tiles should be part of entitymanager?
            for y in self.tiles:
                for x in y:
                    x.dispatch(event)

    def draw(self, display):
        for y in self.tiles:
            for x in y:
                x.draw(display)

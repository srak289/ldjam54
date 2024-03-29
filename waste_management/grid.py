import dataclasses
import pygame
import random

from .entity import Entity
from .event import *
from .player import Player
from .tile import Tile
from .tilemeta import *


@dataclasses.dataclass
class Grid(Entity):
    grid_width: int = 20
    grid_height: int = 10
    tiles: list = dataclasses.field(default_factory=lambda: list())
    player: Player = None
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

        self._special_tiles = set([x for x in TileAttributes.tiles if x.special])

        self._select_exit()
        self._select_keys()
        self._select_glass()

        self.player = Player(0, 0, 30, 30, self.scale)
        self.player.set_tile(self.tiles[0][0])


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
            
            x = random.choice(self.tiles[y])
            while self._special_tiles & x.buf:
                x = random.choice(self.tiles[y])
            x.add_attr(GlassTile)


    def _set_tile_position(self):
        for i, y in enumerate(self.tiles):
            for j, x in enumerate(y):
                # TODO this should account for scale
                # TODO `35` should not be static
                x.set_position(35*j, 35*i)


    def _affect_player(self, event):
        if event.message == "PLAYER_EFFECT_CRUSHED":
            pygame.event.post(GAME_LOSE)
            self.player = None
            return

        if event.message == "PLAYER_EFFECT_DEATH":
            pygame.event.post(GAME_LOSE)
            self.player = None
            return

        # TODO
        self.player.dispatch(event)

        if event.message == "PLAYER_EFFECT_PLAGUE":
            pass
        if event.message == "PLAYER_EFFECT_SLICK":
            pass
        if event.message == "PLAYER_EFFECT_FOOD":
            pass
        if event.message == "PLAYER_EFFECT_KEY":
            pass
        if event.message == "PLAYER_EFFECT_EXIT":
            pass


    def _move_player(self, event):
        # perhaps the player's location is based on tile
        # so the player should maintain a reference to the current tile
        # this would also allow interaction with buffs
        if not self.player:
            return

        cur = self.player.tile

        def find_player():
            for i, y in enumerate(self.tiles):
                for j, x in enumerate(y):
                    if cur == x:
                        return i, j

        i, j = find_player()

        if event == PLAYER_CONTROL_UP:
            i -= 1
        elif event == PLAYER_CONTROL_DOWN:
            i += 1
        elif event == PLAYER_CONTROL_LEFT:
            j -= 1
        elif event == PLAYER_CONTROL_RIGHT:
            j += 1

        if i < 0 or j < 0:
            return

        try:
            dest = self.tiles[i][j]
        except IndexError:
            return

        self.player.set_tile(dest)


    def _collapse(self):
        for y in self.tiles:
            r = []
            for x in y:
                if GlassTile in x.buf:
                    r.append(x)
            for z in r:
                if self.player:
                    if self.player.tile == z:
                        pygame.event.post(PLAYER_EFFECT_CRUSHED)
                y.remove(z)

        self.grid_width -= 1
        self._set_tile_position()
        self._select_glass()


    def dispatch(self, event):
        if event.type == pygame.KEYDOWN:
            if self.player:
                self.player.dispatch(event)
        elif event == GRID_COLLAPSE:
            self._collapse()
            return

        if not hasattr(event, "message"):
            return

        if event.message.startswith("PLAYER_CONTROL"):
            self._move_player(event)
        elif event.message.startswith("PLAYER_EFFECT"):
            self._affect_player(event)
        else:
            # tiles should be part of entitymanager?
            for y in self.tiles:
                for x in y:
                    x.dispatch(event)


    def draw(self, display):
        for y in self.tiles:
            for x in y:
                x.draw(display)
        if self.player:
            self.player.draw(display)


    def run(self):
        if self.player:
            self.player.run()

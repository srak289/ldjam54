import dataclasses
import pygame
import random

from .entity import Entity
from .event import *
from .tile import Tile
from .tilemeta import *


@dataclasses.dataclass
class Player(Entity):

    tile: Tile = None
    hitpoints: int = 3
    keys: int = 0
    inventory: list = dataclasses.field(default_factory=lambda: list())


    def draw(self, display):
        self.surface.fill(self._transparent)
        pygame.draw.circle(
            self.surface,
            self.color,
            ((self._x+self.w)/2, (self._y+self.h)/2),
            self.w/2-5
        )
        display.blit(self.surface, self.rect)


    def setup(self):
        self.margin = 10
        self.buffer = 5
        self._transparent = (255, 0, 255)
        # is the surface set for alpha
        self.surface.set_colorkey(self._transparent)
        self.color = (10, 240, 205)


    def set_tile(self, t: Tile):
        self.tile = t
        self.rect = self.tile.rect


    def dispatch(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP):
                pygame.event.post(PLAYER_UP)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                pygame.event.post(PLAYER_DOWN)
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                pygame.event.post(PLAYER_LEFT)
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                pygame.event.post(PLAYER_RIGHT)
            elif event.key == pygame.K_i:
                pygame.event.post(PLAYER_INVENTORY)

__all__ = ["Player"]

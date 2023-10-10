import dataclasses
import pygame
import random

from .entity import Entity
from .event import *
from .sprite import *
from .tile import Tile
from .tilemeta import *


@dataclasses.dataclass
class Player(Entity):

    tile: Tile = None
    previous_tile: Tile = None
    hitpoints: int = 3
    keys: int = 0
    inventory: list = dataclasses.field(default_factory=lambda: list())


    def setup(self):
        self.margin = 10
        self.buffer = 5
        self.color = (10, 240, 205)


    def dispatch(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP):
                pygame.event.post(PLAYER_CONTROL_UP)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                pygame.event.post(PLAYER_CONTROL_DOWN)
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                pygame.event.post(PLAYER_CONTROL_LEFT)
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                pygame.event.post(PLAYER_CONTROL_RIGHT)
            elif event.key == pygame.K_i:
                pygame.event.post(PLAYER_CONTROL_INVENTORY)
        elif event == PLAYER_EFFECT_KEY:
            self.keys += 1


    def draw(self, display):
        self.surface.fill(self._transparent)
        # something about the border math is probably wrong
        pygame.draw.circle(
            self.surface,
            self.color,
            ((self._x+self.w)/2, (self._y+self.h)/2),
            self.w/2-5
        )
        for h in range(self.hitpoints):
            display.blit(HeartSprite.surface, (10+(32+5)*h, 400))
        for k in range(self.keys):
            display.blit(KeySprite.surface, (10+(32+5)*k, 450))
        display.blit(self.surface, self.rect)


    def run(self):
        # this is broken for tiles recalculating ATTRS
        if self.previous_tile != self.tile:
            for b in self.tile.buf:
                if b.effect:
                    pygame.event.post(b.effect)
            self.previous_tile = self.tile


    def set_tile(self, t: Tile):
        self.tile = t
        self.rect = self.tile.rect

__all__ = ["Player"]

import pygame

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


class Tile(pygame.sprite.Sprite:
    pass


class Grid:

    def __init__(self):
        self._tiles = []

    def get_tile_at(self, x, y):
        try:
            return self._tiles[x][y]
        except IndexArrayError:
            raise

    def blit(self, canvas):
        for row in self._tiles:
            for tile in row:
                canvas.blit(tile.surface, tile.rect)
            
        


class Player:
    pass

class Enemy:
    pass

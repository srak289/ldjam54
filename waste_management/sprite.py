import configparser
import sys

import pygame.image
import pygame.transform
from pygame import Rect, Surface

from .event import *
from .paths import RESOURCES


SHEET = pygame.image.load((RESOURCES / "sprites.png").open())

__all__ = []


class Sprite:

    def __init__(self, **kwargs):
        print(f"Init {self} with {kwargs}")
        x, y = kwargs.pop("location")
        # we don't pop size because Surface constructor needs it
        w, h = kwargs["size"]
        # store the spritesheet location for blitting
        self.rect = Rect(x, y, w, h)

        self.surface = Surface(kwargs["size"])

        self._transparent = (255, 0, 255)
        self.surface.set_colorkey(self._transparent)


    def transform(self, size):
        self.surface = pygame.transform.scale(self.surface, size)
        self.surface.set_colorkey(self._transparent)


c = configparser.ConfigParser()
c.read_string((RESOURCES / "sprites.ini").open().read())

for s in c.sections():
    kwargs = {}
    for k, v in c.items(s):
        if k in ("location", "size"):
            v = tuple(map(int, v.split(",")))
        kwargs[k] = v

    name = f"{s.title()}Sprite"
    newsprite = type(name, (Sprite,), {})(**kwargs)
    newsprite.surface.blit(SHEET, (0, 0), area=newsprite.rect)
    newsprite.transform((32,32))
    locals()[name] = newsprite
    __all__ += [name]

import configparser
import sys

import pygame.image
from pygame import Rect, Surface

from .event import *
from .paths import RESOURCES


SHEET = pygame.image.load((RESOURCES / "sprites.png").open())

__all__ = []


class Sprite(Surface):

    def __init__(self, **kwargs):
        print(f"Init {self} with {kwargs}")
        x, y = kwargs.pop("location")
        # we don't pop size because Surface constructor needs it
        w, h = kwargs["size"]
        # store the spritesheet location for blitting
        self.rect = Rect(x, y, w, h)

        super().__init__(**kwargs)

        self._transparent = (255, 0, 255)
        self.set_colorkey(self._transparent)


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
    newsprite.blit(SHEET, (0, 0), area=newsprite.rect)
    locals()[name] = newsprite
    __all__ += [name]

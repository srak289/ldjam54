import dataclasses
import random

from .entity import Entity
from .event import TILE_SHUF_ATTR
from .tilemeta import *


@dataclasses.dataclass
class Tile(Entity):
    special: bool = False
    sbuf: set = dataclasses.field(default_factory=lambda: set())
    buf: set = dataclasses.field(default_factory=lambda: set())


    def _attr_shuffle(self):
        cur = self.buf
        self.buf = set()


    def setup(self):
        self._attr_shuffle()
        self.color = TileAttributes.NormalTile.rgb_color
        self.surface.fill(self.color)


    def _curcolor(self):
        pass


    def add_char(self, ch: TileCharacteristic):
        """Append a normal characteristic
        """
        self.color = getattr(TileColor, ch.name)
        self.surface.fill(self.color)
        self.buf.add(ch)


    def add_schar(self, ch: TileCharacteristic):
        """Append a special characteristic
        """
        self.color = getattr(TileColor, ch.name)
        self.surface.fill(self.color)
        self.sbuf.add(ch)


    def dispatch(self, event):
        if event == TILE_SHUF_ATTR:
            self._attr_shuffle()
        # elif event == pygame.MOUSEMOVE:
        #     event.self._

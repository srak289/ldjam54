import dataclasses
import random

from .entity import Entity
from .event import TILE_SHUF_ATTR
from .tilemeta import *


@dataclasses.dataclass
class Tile(Entity):
    special: bool = False
    buf: set = dataclasses.field(default_factory=lambda: set())


    def _attr_shuffle(self):
        # we can only shuffle unspecial attrs
        # perhaps we should make sure we cannot regain attrs
        # that we just had on the next clock cycle
        # cur = self.buf
        # self.buf = set()
        pass


    @property
    def color(self):
        # TODO: compute color for multiple bufs
        if self.buf:
            # nasty hack for now
            return next(iter(self.buf)).rgb_color
        else:
            return NormalTile.rgb_color


    def setup(self):
        self._attr_shuffle()
        self.surface.fill(self.color)


    def add_attr(self, attr: TileAttribute):
        """Append an attribute
        """
        if attr.special:
            # do something special
            pass
        self.buf.add(attr)
        self.surface.fill(self.color)


    def dispatch(self, event):
        if event == TILE_SHUF_ATTR:
            self._attr_shuffle()
        # elif event == pygame.MOUSEMOVE:
        #     event.self._
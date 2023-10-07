import dataclasses
import pygame
import random

from .entity import Entity
from .event import TILE_SHUF_ATTR
from .tilemeta import *


@dataclasses.dataclass
class Tile(Entity):
    special: bool = False
    buf: set = dataclasses.field(default_factory=lambda: set())


    def _attr_shuffle(self):
        cur = set()
        for a in self.buf:
            if a.special:
                cur.add(a)
        old = self.buf-cur
        self.buf = cur
        def select():
            f = random.random()
            best = None
            for x in TileAttributes.tiles:
                if f < x.frequency:
                    if best:
                        if x.frequency < best.frequency:
                            best = x
                    else:
                        best = x
            return best

        self.buf.add(select())

        # we can only shuffle unspecial attrs
        # perhaps we should make sure we cannot regain attrs
        # that we just had on the next clock cycle
        # cur = self.buf
        # self.buf = set()


    @property
    def color(self):
        # TODO: compute color for multiple bufs
        if self.buf:
            if GlassTile in self.buf:
                return GlassTile.rgb_color
            else:
                # FIXME
                # nasty hack for now
                return next(iter(self.buf)).rgb_color
        else:
            return NormalTile.rgb_color


    def draw(self, display):
        wid = self.w / len(self.buf)
        breakpoint()
        for b in self.buf:
            t = pygame.Rect(
                self.x,
                self.y,
                wid,
                self._h,
            )
            self.surface.fill(
                b.rgb_color,
            )
            display.blit(self.surface, self.rect)


    def setup(self):
        self.buf.add(NormalTile)
        self._attr_shuffle()


    def add_attr(self, attr: TileAttribute):
        """Append an attribute
        """
        if attr.special:
            # do something special
            pass
        self.buf.add(attr)


    def dispatch(self, event):
        if event == TILE_SHUF_ATTR:
            self._attr_shuffle()
        # elif event == pygame.MOUSEMOVE:
        #     event.self._

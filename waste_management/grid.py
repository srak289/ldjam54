import dataclasses
import enum
import random
import typing

from .entity import Entity
from .event import TILE_SHUF_ATTR


class TileCharacteristic(enum.Enum):
    KEY     = 0
    EXIT    = 1
    FOOD    = 2
    GLASS   = 3
    DEATH   = 4
    PLAGUE  = 5
    SLICK   = 6
    NORMAL  = 10


@dataclasses.dataclass(frozen=True)
class TileBufWeight:
    KEY     = 0.0
    EXIT    = 0.0
    FOOD    = 0.0
    GLASS   = 0.0
    DEATH   = 0.05
    PLAGUE  = 0.25
    SLICK   = 0.50
    NORMAL  = 1.0



@dataclasses.dataclass(frozen=True)
class TileColor:
    PLAYER  = (66, 135, 245)
    KEY     = (197, 207, 60)
    EXIT    = (135, 214, 177)
    FOOD    = (77, 171, 56)
    GLASS   = (252, 169, 114)
    DEATH   = (99, 24, 24)
    PLAGUE  = (191, 152, 44)
    SLICK   = (64, 53, 89)
    NORMAL  = (175, 181, 189)


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
        self.color = TileColor.NORMAL
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



@dataclasses.dataclass
class Grid(Entity):
    grid_width: int = 10
    grid_height: int = 10
    tiles: list = dataclasses.field(default_factory=lambda: list())
    num_keys: int = 5


    def set_size(self, width, height):
        self.grid_width = width
        self.grid_height = height

    def setup(self):
        for x in range(0, self.grid_width):
            self.tiles.append([])
            for y in range(0, self.grid_height):
                self.tiles[x].append(
                    Tile(25*x, 25*y, 20, 20, self.scale)
                )
        self._choose_key()
        self._choose_glass()
        self._choose_exit()


    def _choose_key(self):
        for _ in range(0, self.num_keys):
            x = random.choice(range(0, self.grid_width))
            y = random.choice(range(0, self.grid_height))
            self.tiles[x][y].add_schar(TileCharacteristic.KEY)


    def _choose_glass(self):
        for y in range(0, self.grid_height):
            x = random.choice(range(0, self.grid_width))
            self.tiles[x][y].add_schar(TileCharacteristic.GLASS)


    def _choose_exit(self):
        x = random.choice(range(0, self.grid_width))
        y = random.choice(range(0, self.grid_height))
        self.tiles[x][y].add_schar(TileCharacteristic.EXIT)


    def draw(self, canvas):
        for x in self.tiles:
            for y in x:
                y.draw(canvas)

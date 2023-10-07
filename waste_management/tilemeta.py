import configparser
import importlib.resources


__all__ = []

class TileAttributeMeta(type):
    _tiles = {}
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        if "TileAttribute" in [x.__name__ for x in bases]:
            cls._tiles.update({name: x})
        if name == "TileAttributes":
            for k, v in cls._tiles.items():
                setattr(x, k, v)
            setattr(x, "tiles", tuple(v for v in cls._tiles.values()))
        return x


class TileAttribute(metaclass=TileAttributeMeta): pass

__all__ += ["TileAttribute"]

c = configparser.ConfigParser()

c.read_string(
    importlib.resources.read_text("waste_management.resources", "tiles.ini")
)

for s in c.sections():
    kwargs = {}
    for k, v in c.items(s):
        if k == "rgb_color":
            v = tuple(map(int, v.split(",")))
        kwargs[k] = v

    if "special" not in kwargs:
        kwargs["special"] = False

    if kwargs["special"]:
        # because the grid will assign these tiles
        kwargs["frequency"] = 0

    name = f"{s.title()}Tile"
    newtile = type(name, (TileAttribute,), kwargs)
    locals()[name] = newtile
    __all__ += [name]


class TileAttributes(metaclass=TileAttributeMeta): pass

__all__ += ["TileAttributes"]

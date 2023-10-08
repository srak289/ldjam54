import abc
import dataclasses
import pygame
import random

__all__ = []


@dataclasses.dataclass
class Entity(abc.ABC):
    _x: int
    _y: int
    _w: int
    _h: int
    scale: int = 10
    border: int = 6
    margin: int = 10


    def __post_init__(self):
        self.surface = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.w,
            self.h
        )
        self._transparent = (255, 0, 255)
        self.surface.set_colorkey(self._transparent)
        self.setup()


    def _buffer(self, pos):
        return self.margin + self.border + pos


    def _fit(self, dim):
        return self.scale * dim


    @property
    def w(self):
        return self._w


    @w.setter
    def w(self, n):
        self._w = n


    @property
    def h(self):
        return self._h


    @h.setter
    def h(self, n):
        self._h = h


    @property
    def x(self):
        return self._buffer(self._x)


    @x.setter
    def x(self, n):
        self._x = n
        self.rect.x = self.x


    @property
    def y(self):
        return self._buffer(self._y)


    @y.setter
    def y(self, n):
        self._y = n
        self.rect.y = self.y


    def set_position(self, x, y):
        self.x = x
        self.y = y


    @abc.abstractmethod
    def setup(self):
        """Specific initializations for a subclass of Entity
        """
        raise NotImplementedError


    @abc.abstractmethod
    def dispatch(self, event):
        """Event handling
        """
        raise NotImplementedError


    @abc.abstractmethod
    def draw(self, display):
        raise NotImplementedError

__all__ += ["Entity"]


class EntityManager:
    def __init__(self):
        self._entities = {}


    def dispatch(self, event):
        for entity in self._entities:
            # if the type matches the mask
            entity.dispatch(event)


    def draw(self, display):
        for e in self._entities.values():
            e.draw(display)


    def shutdown(self):
        pass

__all__ += ["EntityManager"]

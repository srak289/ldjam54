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
    border: int = 5
    margin: int = 10


    def _buffer(self, pos):
        return self.margin + self.border + pos


    def _fit(self, dim):
        return self.scale * dim


    def __post_init__(self):
        self.surface = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.w,
            self.h
        )

        self.setup()


    @property
    def w(self):
        return self._w


    @property
    def h(self):
        return self._h


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


    @abc.abstractmethod
    def setup(self):
        raise NotImplementedError


    def set_position(self, x, y):
        self.x = x
        self.y = y


    # blits could stack sprite effects

    def dispatch(self, event):
        if event.type == pygame.WINDOWRESIZE:
            pass
        # handle the event; if it is for us
        pass


    def draw(self, canvas):
        self.surface.fill(self.color)
        canvas.blit(self.surface, self.rect)

__all__ += ["Entity"]


class EntityManager:
    def __init__(self):
        self._entities = {}

    def dispatch(self, event):
        for entity in self._entities:
            # if the type matches the mask
            entity.dispatch(event)

    def draw(self, canvas):
        for e in self._entities.values():
            e.draw(canvas)

    def shutdown(self):
        pass

__all__ += ["EntityManager"]

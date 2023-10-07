import abc
import dataclasses
import pygame
import random

__all__ = []


@dataclasses.dataclass
class Entity(abc.ABC):
    x: int
    y: int
    w: int
    h: int
    scale: int = 10
    border: int = 5
    margin: int = 10


    def _buffer(self, pos):
        return self.margin + self.border + pos


    def _stretch(self, dim):
        return self.scale * dim


    def __post_init__(self):
        self.surface = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(
            self._buffer(self.x),
            self._buffer(self.y),
            self.w,
            self.h
        )

        self.setup()


    @abc.abstractmethod
    def setup(self):
        raise NotImplementedError


    def set_position(self, x, y):
        self.rect.x = self._buffer(x)
        self.rect.y = self._buffer(y)


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

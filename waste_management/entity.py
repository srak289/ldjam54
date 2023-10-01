import pygame
import random

__all__ = []


class Entity:
    def __init__(self, x, y, w, h, scale):
        self._scale = scale
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self.surface = pygame.Surface((w, h))
        self._color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.surface.fill(self.color)
        self.rect = pygame.Rect(x, y, w, h)
        print(f"Creating entity {self} at {x} {y} size {w} {h}")


    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y


    @property
    def w(self):
        return self._w


    @property
    def h(self):
        return self._h


    @property
    def scale(self):
        return self._scale


    @property
    def color(self):
        return self._color


    def set_position(self, x, y):
        self._x = x
        self._y = y


    # blits could stack sprite effects

    def dispatch(self, event):
        if event.type == pygame.WINDOWRESIZE:
            pass
        # handle the event; if it is for us
        pass


    def draw(self, canvas):
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

import dataclasses
import pygame
import random

__all__ = []


@dataclasses.dataclass
class Entity:
    x: int
    y: int
    w: int
    h: int
    scale: int = 10
    surface: pygame.Surface = None
    rect: pygame.Rect = None
    color: tuple = None

    def __post_init__(self):
        self.surface = pygame.Surface((w, h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.surface.fill(self.color)
        self.rect = pygame.Rect(x, y, w, h)
        print(f"Creating entity {self} at {x} {y} size {w} {h}")


    def set_position(self, x, y):
        self.rect.move(x, y)


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

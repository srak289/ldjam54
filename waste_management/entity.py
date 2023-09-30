import pygame


__all__ = []


class Entity:
    def __init__(self, x, y, scale):
        self._scale = scale
        self._x = x
        self._y = y
        self.surface = pygame.Surface((x, y))
        self._color = (0, 127, 0)
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect()


    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y


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

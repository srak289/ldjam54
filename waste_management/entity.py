import pygame


__all__ = []


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        self._event_filter = set()
        pass


    def dispatch(self, event):
        # handle the event; if it is for us
        pass

__all__ += ["Entity"]


class EntityManager:
    def __init__(self):
        self._entities = {}

    def dispatch(self, event):
        for entity in self._entities:
            # if the type matches the mask
            entity.dispatch(event)

__all__ += ["EntityManager"]

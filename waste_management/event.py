import pygame.event

class GameEvent:
    def __init__(self):
        self.n = pygame.USEREVENT

    def __iter__(self):
        return self

    def __next__(self):
        cur, self.n = self.n, self.n + 1
        return cur

    def new(self, **kwargs):
        return pygame.event.Event(
            next(self),
            **kwargs,
        )

ge = GameEvent()


GAME_STOP = ge.new(message="GAME_STOP")

GAME_RUN = ge.new(message="GAME_RUN")

MENU_STOP = ge.new(message="MENU_STOP")

MENU_RUN = ge.new(message="MENU_RUN")

TILE_SHUF_ATTR = ge.new(message="TILE_SHUF_ATTR")

GRID_COLLAPSE = ge.new(message="GRID_COLLAPSE")


__all__ = ["GAME_STOP", "GAME_RUN", "MENU_STOP", "MENU_RUN"]

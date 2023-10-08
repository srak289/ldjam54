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


PLAYER_UP = ge.new(message="PLAYER_UP")
PLAYER_DOWN = ge.new(message="PLAYER_DOWN")
PLAYER_LEFT = ge.new(message="PLAYER_LEFT")
PLAYER_RIGHT = ge.new(message="PLAYER_RIGHT")
PLAYER_INVENTORY = ge.new(message="PLAYER_INVENTORY")

PLAYER_CRUSHED = ge.new(message="PLAYER_CRUSHED")
PLAYER_KILLED = ge.new(message="PLAYER_KILLED")
PLAYER_INJURED = ge.new(message="PLAYER_INJURED")
PLAYER_INFECTED = ge.new(message="PLAYER_INFECTED")
PLAYER_SLIP = ge.new(message="PLAYER_SLIP")
PLAYER_PICKUP = ge.new(message="PLAYER_PICKUP")

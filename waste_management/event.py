from pygame import USEREVENT
from pygame.event import Event


i = USEREVENT

for n in (
    "GAME_STOP",
    "GAME_RUN",

    "MENU_STOP",
    "MENU_RUN",


    "TILE_SHUF_ATTR",


    "GRID_COLLAPSE",


    "PLAYER_UP",
    "PLAYER_DOWN",
    "PLAYER_LEFT",
    "PLAYER_RIGHT",
    "PLAYER_INVENTORY",

    "PLAYER_CRUSHED",
    "PLAYER_KILLED",
    "PLAYER_INJURED",
    "PLAYER_INFECTED",
    "PLAYER_SLIP",
    "PLAYER_PICKUP",
):
    i += 1
    locals()[n] = Event(i, message=n)

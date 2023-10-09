from pygame import USEREVENT
from pygame.event import Event


i = USEREVENT

for n in (
    "GAME_STOP",
    "GAME_RUN",
    "GAME_WIN",
    "GAME_LOSE",

    "MENU_STOP",
    "MENU_RUN",


    "TILE_SHUF_ATTR",


    "GRID_COLLAPSE",


    "PLAYER_CONTROL_UP",
    "PLAYER_CONTROL_DOWN",
    "PLAYER_CONTROL_LEFT",
    "PLAYER_CONTROL_RIGHT",
    "PLAYER_CONTROL_INVENTORY",

    "PLAYER_EFFECT_CRUSHED",
    "PLAYER_EFFECT_KILLED",
    "PLAYER_EFFECT_INJURED",
    "PLAYER_EFFECT_INFECTED",
    "PLAYER_EFFECT_SLIP",
    "PLAYER_EFFECT_PICKUP",
):
    i += 1
    locals()[n] = Event(i, message=n)

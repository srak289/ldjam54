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

    "PLAYER_EFFECT_DEATH",
    "PLAYER_EFFECT_PLAGUE",
    "PLAYER_EFFECT_SLICK",
    "PLAYER_EFFECT_FOOD",
    "PLAYER_EFFECT_KEY",
    "PLAYER_EFFECT_EXIT",
):
    i += 1
    locals()[n] = Event(i, message=n)

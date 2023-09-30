import pygame.event

GAME_STOP = pygame.event.Event(
    pygame.USEREVENT + 1,
    message="GAME_STOP"
)

GAME_RUN = pygame.event.Event(
    pygame.USEREVENT + 2,
    message="GAME_RUN"
)

MENU_STOP = pygame.event.Event(
    pygame.USEREVENT + 3,
    message="MENU_STOP"
)

MENU_RUN = pygame.event.Event(
    pygame.USEREVENT + 4,
    message="MENU_RUN"
)

__all__ = ["GAME_STOP", "GAME_RUN", "MENU_STOP", "MENU_RUN"]

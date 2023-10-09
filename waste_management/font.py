import importlib.resources

import pygame.font
pygame.font.init()

RESOURCE_BASE = importlib.resources.files("waste_management.resources")

foxbot = pygame.font.Font(
    str(RESOURCE_BASE / "Foxbot.ttf"),
    60,
)

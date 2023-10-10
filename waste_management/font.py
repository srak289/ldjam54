import importlib.resources

import pygame.font
pygame.font.init()

RESOURCE_BASE = importlib.resources.files("waste_management.resources")


__all__ = []


class FoxBot(pygame.font.Font):

    def draw_text(
        self,
        display: pygame.Surface,
        text: str,
        color: tuple = (255, 0, 0),
        rect: pygame.Rect = None
    ) -> None:
        """Draw text starting at the given coordinates
        Args:
            display(pygame.Surface): The surface to draw to

            text(str): The text to render

            color(tuple): (r, g, b) color
                default = (255, 0, 0)

            rect(pygame.Rect): Specify text location / size
                `display.get_rect().center` is used if rect is `None`
                default = None
        """
        textwidth, textheight = self.size(text)
        text = self.render(text, False, color)
        x, y = display.get_rect().center

        display.blit(text, (x - textwidth / 2, y - textheight / 2))


foxbot = FoxBot(
    str(RESOURCE_BASE / "Foxbot.ttf"),
    60,
)

__all__ += ["foxbot"]

import pygame
import sys

from .app import *


class WindowManager:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self._menu = Menu()
        self._game = Game()
        self._load = Load()
    

    @property
    def running_app(self):
        if self._game.state == AppState.RUN:
            return self._game
        elif self._menu.state == AppState.RUN:
            return self._menu
        else:
            if not self._menu.state == AppState.SHUTDOWN:
                self._menu.setup()
            return self._load

    
    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                print(f"Recieved event {event}")
                self._game.call_dispatch(event)
                self._menu.call_dispatch(event)
                self._load.call_dispatch(event)

            self.running_app.call_draw(self.display)
            self.running_app.run()

            pygame.event.pump()

            pygame.display.update()
            self.clock.tick(60)


wm = WindowManager()

import pygame
import sys

from .app import *


class WindowManager:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((400, 600), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        # dispatch events to entities in our game so they can interact
        # handle win  conditions and scoring
        # handle graceful shutdown of the game (this means simply destroying everything)
        # 
        self._menu = Menu()
        self._game = Game()
        self._loading = Loading()
    

    @property
    def running_app(self):
        if self._game.state == AppState.RUN:
            return self._game
        elif self._menu.state == AppState.RUN:
            return self._menu
        else:
            return self._loading

    
    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                print(f"Recieved event {event}")
                self.running_app.dispatch(event)

            self.running_app.draw(self.display)
            self.running_app.run()

            pygame.display.update()
            self.clock.tick(60)


wm = WindowManager()

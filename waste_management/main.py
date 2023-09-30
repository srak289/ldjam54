import sys

import pygame
from pygame.locals import *

class EntityManager:
    def __init__(self):
        self._entities = []

    def register(self, handle):
        pass
    def deregister(self, handle):
        pass
    def dispatch(self, event):
        for e in self._entities:
            e.notify(event)


class GameMode(enum.Enum):
    TURN_BASED = 0
    TIME_BASED = 1
    ACTION_BASED = 2


class Game:
    def __init__(
        self,
        game_mode,
    ):
        pygame.init()
        self.display = pygame.display.set_mode((400, 600))
        self.clock = pygame.time.Clock()

        # dispatch events to entities in our game so they can interact
        # handle win  conditions and scoring
        # handle graceful shutdown of the game (this means simply destroying everything)
        # 
        self._entities = {}

    def dispatch(self, event):
        # the mask is a | style for event types listened for as registered

    def register_entity(self, eid, event_mask):
        self._entities.update(

    def deregister_entity(self, eid, event_mask):


    def get_entity(self, eid):
        pass

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.dispatch(event)

            self.display.update()
            self.clock.tick(60)


    def shutdown(self):
        pass


g = Game()
g.run()

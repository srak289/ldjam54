import enum
import pygame

from .entity import *


class GameMode(enum.Enum):
    TURN_BASED = 0
    TIME_BASED = 1
    ACTION_BASED = 2


class AppState(enum.Enum):
    RUN = 0
    PAUSE = 1
    SHUTDOWN = 2
    INIT = 4


class Application:
    def __init__(self):
        self.entity_manager = EntityManager()
        self._state = AppState.INIT


    @property
    def state(self):
        return self._state


    def main_loop(self):
        raise NotImplementedError


    def setup(self):
        raise NotImplementedError


    def draw(self, canvas):
        self.entity_manager.draw(canvas)


    def dispatch(self, event):
        # if it is not for us just dispatch it
        self.entity_manager.dispatch(event)


    def shutdown(self):
        self.entity_manager.shutdown()



class Game(Application):
    pass


class Menu(Application):
    pass


class Loading(Application):
    def draw(self, canvas):
        canvas.fill((127, 127, 127))

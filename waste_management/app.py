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


    def run(self):
        """This is the main loop"""
        raise NotImplementedError


    def setup(self):
        raise NotImplementedError


    def draw(self, canvas):
        self.entity_manager.draw(canvas)


    def dispatch(self, event):
        self.entity_manager.dispatch(event)


    def shutdown(self):
        self.entity_manager.shutdown()



class Game(Application):
    def __init__(self):
        self._menu = None


    def setup(self, **kwargs):
        if "menu" in kwargs:
            self._menu = kwargs.pop("menu")


    def draw(self, canvas):
        canvas.fill((127, 0, 127))

    def dispatch(self, event):
        if event.type == :

        if event.type == pygame.K_J:
            self._state = AppState.STOP
            pygame.event.push(pygame.event.Event("GameStop"))
        super().dispatch(event)



    def run(self):
        pass


class Menu(Application):
    def __init__(self):
        self._game = None


    def setup(self, **kwargs):
        if "game" in kwargs:
            self._game = kwargs.pop("game")
        self._state = AppState.RUN


    def draw(self, canvas):
        canvas.fill((0, 127, 127))


    def dispatch(self, event):
        if event.type == pygame.K_J:
            self._state = AppState.STOP
            pygame.event.push(pygame.event.Event("GameRun"))
        super().dispatch(event)

    def run(self):
        pass


class Loading(Application):
    def draw(self, canvas):
        canvas.fill((127, 127, 127))


    def run(self):
        pass

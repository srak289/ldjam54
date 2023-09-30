import enum
import pygame

from .entity import *
from .event import *


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


    def call_dispatch(self, event):
        self.dispatch(event)
        if self.state == AppState.RUN:
            self.entity_manager.dispatch(event)


    def setup(self):
        """This method must set self._state to AppState.RUN"""
        raise NotImplementedError


    def call_draw(self, canvas):
        if self.state == AppState.RUN:
            self.draw(canvas)
            self.entity_manager.draw(canvas)


    def draw(self, canvas):
        raise NotImplementedError


    def dispatch(self, event):
        raise NotImplementedError


    def shutdown(self):
        self._state = AppState.SHUTDOWN
        self.entity_manager.shutdown()



class Game(Application):
    def setup(self):
        self._state = AppState.RUN
        print("RUNNING GAME")


    def draw(self, canvas):
        canvas.fill((127, 0, 127))

    def dispatch(self, event):
        if event.type == GAME_RUN:
            self.setup()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                self.shutdown()
            pygame.event.post(GAME_STOP)


    def run(self):
        pass


class Menu(Application):
    def setup(self):
        self._state = AppState.RUN


    def draw(self, canvas):
        canvas.fill((0, 127, 127))


    def dispatch(self, event):
        if event.type == GAME_STOP:
            self.setup()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                self.shutdown()
            pygame.event.post(GAME_RUN)

    def run(self):
        pass


class Load(Application):
    def setup(self):
        self._state = AppState.RUN
        # whatever loading here
        pygame.event.post(MENU_RUN)


    def draw(self, canvas):
        canvas.fill((127, 127, 127))


    def dispatch(self, event):
        pass


    def run(self):
        pass

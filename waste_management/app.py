import enum
import pygame

from .entity import *
from .event import *
from .grid import Grid


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


    def call_dispatch(self, event):
        self.dispatch(event)
        if self.state == AppState.RUN:
            self.entity_manager.dispatch(event)


    def call_draw(self, display):
        if self.state == AppState.RUN:
            self.draw(display)
            #self.entity_manager.draw(display)
            # there should be an order to blit or we could draw over something else


    def setup(self):
        """This method must set self._state to AppState.RUN"""
        raise NotImplementedError


    def run(self):
        """This is the main loop"""
        raise NotImplementedError


    def draw(self, display):
        raise NotImplementedError


    def dispatch(self, event):
        raise NotImplementedError


    def shutdown(self):
        self._state = AppState.SHUTDOWN
        self.entity_manager.shutdown()



class Game(Application):
    def setup(self):
        self.grid = Grid(0, 0, 120, 120, 1, 20, 10)
        self._state = AppState.RUN
        self.ticks = 0


    def draw(self, display):
        display.fill((0, 0, 0))
        self.grid.draw(display)


    def dispatch(self, event):
        if event == GAME_RUN:
            if not self.state == AppState.RUN:
                self.setup()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                self.shutdown()
                pygame.event.post(GAME_STOP)
        # we should really have the entity_manager dispatching to tiles
        if (
            event in [TILE_SHUF_ATTR, GRID_COLLAPSE, PLAYER_UP, PLAYER_DOWN, PLAYER_LEFT, PLAYER_RIGHT]
            or event.type in [pygame.KEYDOWN]
        ):
            if hasattr(self, "grid"):
                self.grid.dispatch(event)


    def run(self):
        # main loop
        self.ticks += 1
        if self.ticks % (60 * 2) == 0:
            pygame.event.post(TILE_SHUF_ATTR)
        if self.ticks % (60 * 5) == 0:
            pygame.event.post(GRID_COLLAPSE)


class Menu(Application):
    def setup(self):
        self._state = AppState.RUN


    def draw(self, display):
        display.fill((0, 127, 127))


    def dispatch(self, event):
        if event == GAME_STOP:
            if not self.state == AppState.RUN:
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


    def draw(self, display):
        display.fill((127, 127, 127))


    def dispatch(self, event):
        pass


    def run(self):
        pass

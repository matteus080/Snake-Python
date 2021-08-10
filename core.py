import pygame as pg
import numpy as np

pg.init()
# pg.mouse.set_visible(False)

class Input:
    """
    A class for getting input easier. Provides options for using indexing of a
    class instance to find out whether or not a button was pressed last frame.

    Only one instance of this class should only be instantiated at a time.
    """

    def __init__(self):
        self.pressed = ...
        self.events = ...

    def get(self) -> None:
        """Updates the `pressed` and `events` attributes."""

        self.pressed = pg.key.get_pressed()
        self.events = pg.event.get()
        self.mouse_pos = np.array(pg.mouse.get_pos())

    def __getitem__(self, index) -> list:
        """
        Takes in one and more slices and filters the list stored in the
        `events` attribute from left to right, returning the filtered list.

        Example
        -------
        >>> # Returns all pg.events k such that k.type == pg.QUIT
        >>> Game.input["type": pg.QUIT]
        >>>
        >>> # Same as above except k.type == pg.KEYDOWN and k.key == pg.K_x
        >>> Game.input["type": pg.KEYDOWN, "key": pg.K_x]
        """

        if isinstance(index, slice):
            return [i for i in self.events if getattr(i, index.start) == index.stop]

        if isinstance(index, tuple):
            events_ = self.events.copy()
            for slice_ in index:
                events_ = [i for i in events_ if getattr(i, slice_.start) == slice_.stop]
            return events_

        raise TypeError(
            f"Indices must be integers or dictionaries, not {type(index)}.")


class Screen:
    size = np.array((1920 // 8, 1080 // 8))
    screen = pg.display.set_mode(size, pg.SCALED | pg.FULLSCREEN)
    rect = screen.get_rect()

    bounds = np.array([size[1]] * 2, dtype=int) - 40
    bounds_rect = pg.Rect((0, 0), bounds)
    bounds_rect.center = size // 2


class Game:
    frame = 0
    fps = 60
    run = True
    states = {}

    input = Input()
    clock = pg.time.Clock()

    @classmethod
    def update(cls):
        cls.frame += 1
        cls.input.get()

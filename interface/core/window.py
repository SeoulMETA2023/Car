import pygame


class Window:
    """manage monitor window"""

    def __init__(self):
        # window mode app size
        self._window_size: tuple[int, int] = (800, 500)
        # current app size
        self._display_size: tuple[int, int] = (800, 500)
        # monitor size for full screen mode
        self._monitor_size: tuple[int, int] = (pygame.display.Info().current_w, pygame.display.Info().current_h)

        # surfaces
        self._window: pygame.Surface = pygame.display.set_mode(self._window_size)
        self._display: pygame.Surface = pygame.Surface(self._display_size)

        self._is_full: bool = False

    @property
    def display_size(self) -> tuple[int, int]:
        return self._display_size

    @property
    def window(self) -> pygame.Surface:
        return self._window

    @property
    def display(self) -> pygame.Surface:
        return self._display

    @property
    def is_full(self) -> bool:
        return self._is_full

    def set_full_mode(self) -> None:
        """set app to fullscreen mode"""
        self._display_size = self._monitor_size
        self._is_full = True
        pygame.display.set_mode(self._display_size, pygame.FULLSCREEN)
        return

    def set_window_mode(self) -> None:
        """set app to window mode"""
        self._display_size = self._window_size
        self._is_full = False
        pygame.display.set_mode(self._display_size)
        return

from pygame import Surface,font, time
from src.Button import Button
from abc import ABC, abstractmethod

class Ui(ABC):
    def __init__(self,
                 screen: Surface,
                 buttons: list[Button], 
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock):
        self._screen = screen
        self._buttons = buttons
        self._fonts = fonts   
        self._clock = clock
    
    @abstractmethod
    def run(self):
        pass
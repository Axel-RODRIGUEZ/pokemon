from pygame import Surface,font
from src.Button import Button
from src.User import User
from abc import ABC, abstractmethod

class Ui(ABC):
    def __init__(self,
                 screen: Surface,
                 buttons: list[Button], 
                 fonts: list[font.Font, font.Font]):
        self._screen = screen
        self._buttons = buttons
        self._fonts = fonts   
    
    @abstractmethod
    def run(self):
        pass
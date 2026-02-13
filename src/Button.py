from pygame import Rect

class Button:

    def __init__(self,
                 target_name: str,
                 lefttop: tuple[int,int],
                 widthheight: tuple[int,int] = (300,60),
                 text: str = "", 
                 color: tuple[int,int,int] = (100,100,200),  
                 hover_color: tuple[int,int,int] = (50,50,100),
                 font_color: tuple[int,int,int] = (255,255,255),
                 hover_font_color: tuple[int,int,int] = (255,255,200)
                 ):

        if isinstance(lefttop, tuple): 
            self.lefttop = lefttop
            if isinstance(widthheight, tuple):
                self.rect = Rect(lefttop,widthheight)
                self.widthheight = widthheight
                if isinstance(text, str):
                    self.text = text
                    if isinstance(target_name, str):
                        self.__target_name = target_name
                        if isinstance(color, tuple):
                            self.__color = color
                            self.current_color = color
                            if isinstance(hover_color, tuple):
                                self.__hover_color = hover_color
                                if isinstance(font_color, tuple):
                                    self.__font_color = font_color
                                    self.current_font_color = font_color
                                    if isinstance(hover_font_color, tuple):
                                        self.__hover_font_color = hover_font_color
                                    else:
                                        raise Exception("Button.__init__(): hover_font_color should be a tuple of int: (int,int,int).")
                                else:
                                    raise Exception("Button.__init__(): font_color shoud be a tuple of int: (int,int,int).")
                            else:
                                raise Exception("Button.__init__(): hover_color should be a tuple of int: (int,int,int).")
                        else:
                            raise Exception("Button.__init__(): color should be a tuple of int: (int,int,int).")
                    else:
                        raise Exception("Button.__init__(): target_name should be a str.")
                else:
                    raise Exception("Button.__init__(): text should be a str.")
            else:
                raise Exception("Button.__init__(): widthheight should be a tuple of int: (int,int).")
        else:
            raise Exception("Button.__init__(): lefttop should be a tuple of int: (int,int).")

    def get_target_name(self):
        return self.__target_name
    
    def get_color(self):
        return self.__color
    
    def get_hover_color(self):
        return self.__hover_color
    
    def get_font_color(self):
        return self.__font_color
    
    def get_hover_font_color(self):
        return self.__hover_font_color

    def hovered(self):
        self.current_color = self.__hover_color
        self.current_font_color = self.__hover_font_color

    def avoided(self):
        self.current_color = self.__color
        self.current_font_color = self.__font_color
from pygame import Rect,Surface

class Button:

    def __init__(self,
                 fonts: tuple,
                 screen: Surface,
                 target_name: str,
                 topleft: tuple[int,int],
                 widthheight: tuple[int,int] = (250,60),
                 text: str = "", 
                 color: tuple[int,int,int] = (100,100,200),  
                 hover_color: tuple[int,int,int] = (50,50,100),
                 font_color: tuple[int,int,int] = (255,255,255),
                 hover_font_color: tuple[int,int,int] = (255,255,200)
                 ):
        if isinstance(fonts,tuple):
            self.__fonts = fonts
            if isinstance(screen, Surface):
                self.__screen = screen
                if isinstance(topleft, tuple): 
                    if isinstance(widthheight, tuple):
                        self.__rect = Rect(topleft,widthheight)
                        self.__surface = Surface(widthheight)
                        if isinstance(text, str):
                            self.__text = text
                            if isinstance(target_name, str):
                                self.__target_name = str
                                if isinstance(color, tuple):
                                    self.__color = color
                                    self.__current_color = color
                                    if isinstance(hover_color, tuple):
                                        self.__hover_color = hover_color
                                        if isinstance(font_color, tuple):
                                            self.__font_color = font_color
                                            self.__current_font_color = font_color
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
                    raise Exception("Button.__init__(): topleft should be a tuple of int: (int,int).")
            else:
                raise Exception("Button.__init__(): screen should be a pygame Surface instance.")
        else:
                raise Exception("Button.__init__(): fonts should be a tuple of pygame Font instances (font,font).")
        
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
    
    def draw(self):
        self.__surface.fill(self.__current_color)
        if self.__text != "":
            text_surf = self.__fonts[0].render(self.__text, True, self.__current_font_color)
            self.__surface.blit(text_surf, text_surf.get_rect(center = self.__surface.get_rect().center))
        self.__screen.blit(self.__surface, (self.__rect.x, self.__rect.y))

    def hovered(self):
        self.__current_color = self.__hover_color
        self.__current_font_color = self.__hover_font_color

    def avoided(self):
        self.__current_color = self.__color
        self.__current_font_color = self.__font_color

    def get_rect(self):
        return self.__rect
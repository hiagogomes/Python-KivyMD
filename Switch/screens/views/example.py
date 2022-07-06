from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class Troca(MDScreen, MDApp):
    
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

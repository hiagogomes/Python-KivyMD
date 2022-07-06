import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/views/troca.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "Troca": "screens.views.example",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.theme_style = 'Light'
        return Factory.MainScreenManager()

if __name__ == "__main__":
    LiveApp().run()

'''
    GUI for PyKLogger Application
    Author: Ada92
'''
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Color

import pyklogger

Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 150)

class PyKLogger(Widget):
    def on_start(self):
        pyklogger.start()
        self.ids.status.text = "Recording..."
        self.ids.status.color = (1, 0, 0, 1)


    def on_stop(self):
        pyklogger.stop()
        self.ids.status.text = "--Stopped--"
        self.ids.status.color = (0, 1, 0, 1)


class PyKLoggerApp(App):
    def build(self):
        return PyKLogger()


if __name__ == '__main__':
    PyKLoggerApp().run()
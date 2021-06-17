from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class MainStackLayout(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b = Button(text="Home",size_hint=(.1,.1))
        b2 = Button(text="TITLE",size_hint=(.9,.1))
        self.add_widget(b)
        self.add_widget(b2)

class PracticeApp(App):
    pass

PracticeApp().run()
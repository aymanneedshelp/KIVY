from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(10):
            b = Button(text=str(i+1),size_hint=(.2,.2))
            self.add_widget(b)

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

TheLabApp().run()
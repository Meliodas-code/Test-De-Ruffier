from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty
from kivy.clock import Clock

#intento de hacer algo pero , frustracion = chatgpt 

class Seconds(Label):
    done = BooleanProperty(False)
    current = NumericProperty(0)
    total = NumericProperty(0)

    def __init__(self, total=10, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.text = str(self.total)
        self.current = 0

    def restart(self, total=None):
        if total:
            self.total = total
        self.current = 0
        self.done = False
        self.text = str(self.total)

    def start(self):
        self.current = 0
        self.done = False
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        remaining = self.total - self.current
        self.text = str(max(remaining, 0))
        if self.current >= self.total:
            self.done = True
            return False  # Detener intervalo
        return True

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from seconds import Seconds
from ruffier import test
import instructions as instr
#ten Fe de que funcione

#bariables gloables
name = ""
age = 0
p1 = 0
p2 = 0
p3 = 0

#que asco de codigo tio , que ansiedad me da ver esto
class SiguienteButton(Button):
    def __init__(self, screen, target_screen, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.target_screen = target_screen
        self.bind(on_release=self.change_screen)

    def change_screen(self, *args):
        self.screen.manager.current = self.target_screen


# voy a comentar todo porque me aburro ok ??? 
# esto es la pantalla de las instrucciones en la que pones tus datos y se guardan ( epico )
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20)

        layout.add_widget(Label(text=instr.txt_instruction))

        #esto es el nombre porque es muy necesario (enserio)
        self.input_name = TextInput(hint_text="Nombre", multiline=False)
        layout.add_widget(self.input_name)

        # introducir tu edad jajaj 👶🍼
        self.input_age = TextInput(hint_text="Edad", multiline=False, input_filter='int')
        layout.add_widget(self.input_age)

        #el boton de siguiente para darle a siguiente tu sabes lo que digo
        btn_next = Button(text="Siguiente")
        btn_next.bind(on_release=self.save_data)
        layout.add_widget(btn_next)

        self.add_widget(layout)
    # esto todos sabesmos lo que es la verdad
    def save_data(self, *args):
        global name, age
        name = self.input_name.text
        try:
            age = int(self.input_age.text)
        except:
            age = 0
        self.manager.current = 'pulse1'

#esto lo pedia la documentacion pero por mi borraba el codigo entero la verdad

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20)
        layout.add_widget(Label(text=instr.txt_test1))
        self.timer = Seconds(total=15)
        layout.add_widget(self.timer)
        btn_next = SiguienteButton(self, 'sits', text="Siguiente")
        layout.add_widget(btn_next)
        self.add_widget(layout)

    def on_enter(self, *args):
        # Reiniciar el temporizador cada vez que entramos a esta pantalla pq habia un bug
        self.timer.restart(15)
        self.timer.start()



# adivina la pelicula 💀😇🥳
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20)
        layout.add_widget(Label(text=instr.txt_sits))
        btn_next = SiguienteButton(self, 'pulse2', text="Siguiente")
        layout.add_widget(btn_next)
        self.add_widget(layout)

# ya me aburri pero esto calcula el resultado 
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20)
        layout.add_widget(Label(text=instr.txt_test3))


        self.input_p1 = TextInput(hint_text="Pulso 1", multiline=False, input_filter='int')
        self.input_p2 = TextInput(hint_text="Pulso 2", multiline=False, input_filter='int')
        self.input_p3 = TextInput(hint_text="Pulso 3", multiline=False, input_filter='int')

        layout.add_widget(self.input_p1)
        layout.add_widget(self.input_p2)
        layout.add_widget(self.input_p3)

        btn_next = Button(text="Calcular Resultado")
        btn_next.bind(on_release=self.save_pulses)
        layout.add_widget(btn_next)

        self.add_widget(layout)
    #simplemente increible
    def save_pulses(self, *args):
        global p1, p2, p3
        try:
            p1 = int(self.input_p1.text)
        except:
            p1 = 0
        try:
            p2 = int(self.input_p2.text)
        except:
            p2 = 0
        try:
            p3 = int(self.input_p3.text)
        except:
            p3 = 0
        self.manager.current = 'result'

#result
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20)
        self.label = Label(text="")
        layout.add_widget(self.label)

        btn_restart = Button(text="Reiniciar")
        btn_restart.bind(on_release=lambda *args: App.get_running_app().reset())
        layout.add_widget(btn_restart)

        self.add_widget(layout)

    def on_enter(self, *args):
        global name, age, p1, p2, p3
        resultado = test(p1, p2, p3, age)
        self.label.text = f"Hola {name}, {resultado}"


#app :)

class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(InstrScr(name='instr'))
        self.sm.add_widget(PulseScr(name='pulse1'))
        self.sm.add_widget(CheckSits(name='sits'))
        self.sm.add_widget(PulseScr2(name='pulse2'))
        self.sm.add_widget(Result(name='result'))
        return self.sm

    def reset(self):
        # Limpiar variables globales
        global name, age, p1, p2, p3
        name = ""
        age = 0
        p1 = 0
        p2 = 0
        p3 = 0

        # Reconstruir las pantallas
        self.sm.clear_widgets()
        self.sm.add_widget(InstrScr(name='instr'))
        self.sm.add_widget(PulseScr(name='pulse1'))
        self.sm.add_widget(CheckSits(name='sits'))
        self.sm.add_widget(PulseScr2(name='pulse2'))
        self.sm.add_widget(Result(name='result'))
        self.sm.current = 'instr'



if __name__ == '__main__':
    MyApp().run()

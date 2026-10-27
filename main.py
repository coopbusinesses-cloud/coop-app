 from kivy.app import App
from kivy.uix.label import Label

class CoopApp(App):
    def build(self):
        return Label(text='COOP Savings App - Working!')

CoopApp().run()
 from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CoopApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text='COOP Savings', font_size=30, size_hint_y=0.3))
        layout.add_widget(Label(text='Welcome!', font_size=20))
        
        self.input_name = TextInput(hint_text='Member Name', size_hint_y=0.2)
        self.input_amount = TextInput(hint_text='Savings Amount', input_filter='float', size_hint_y=0.2)
        
        btn = Button(text='Add Savings', size_hint_y=0.2, background_color=(0,0.7,0,1))
        btn.bind(on_press=self.add_savings)
        
        self.result = Label(text='Total: P0.00', font_size=18)
        
        layout.add_widget(self.input_name)
        layout.add_widget(self.input_amount)
        layout.add_widget(btn)
        layout.add_widget(self.result)
        
        self.total = 0
        return layout
    
    def add_savings(self, instance):
        try:
            amount = float(self.input_amount.text or 0)
            self.total += amount
            self.result.text = f"Total: P{self.total:.2f}\nThanks {self.input_name.text}!"
            self.input_amount.text = ""
        except:
            self.result.text = "Enter valid amount"

CoopApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import os
from datetime import datetime

class CoopApp(App):
    def build(self):
        self.sd = self.get_sd()
        self.file = os.path.join(self.sd, "COOP_SAVINGS.txt")
        b = BoxLayout(orientation='vertical', padding=20, spacing=10)
        b.add_widget(Label(text=f"Save to:\n{self.file}", font_size=11, size_hint_y=0.3))
        self.name = TextInput(hint_text="Member Name", multiline=False, size_hint_y=0.2)
        self.amt = TextInput(hint_text="Amount", multiline=False, size_hint_y=0.2)
        btn = Button(text="SAVE TO SD CARD", size_hint_y=0.3, background_color=(0,0.6,0,1))
        btn.bind(on_press=self.save)
        b.add_widget(self.name)
        b.add_widget(self.amt)
        b.add_widget(btn)
        return b
    def get_sd(self):
        for base in ["/storage","/mnt/media_rw"]:
            if os.path.exists(base):
                try:
                    for d in os.listdir(base):
                        f=os.path.join(base,d)
                        if "-" in d and os.path.isdir(f) and os.access(f, os.W_OK):
                            return f
                except: pass
        return "/storage/emulated/0/Download"
    def save(self, x):
        n=self.name.text.strip()
        a=self.amt.text.strip()
        if not n or not a:
            self.pop("Fill name and amount");return
        try:
            os.makedirs(os.path.dirname(self.file), exist_ok=True)
            with open(self.file,"a") as f:
                f.write(f"{datetime.now()} | {n} | {a}\n")
            self.pop(f"Saved!\n{self.file}")
            self.name.text="";self.amt.text=""
        except Exception as e:
            self.pop(f"Error: {e}\nAllow All Files in Settings")
    def pop(self,m):
        Popup(title="Coop",content=Label(text=m),size_hint=(0.8,0.5)).open()
CoopApp().run()

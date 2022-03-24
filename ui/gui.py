from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
# The ProgressBar widget is used to
# visualize the progress of some task
from kivy.uix.progressbar import ProgressBar

# BoxLayout arranges children in a vertical or horizontal box. 
# or help to put the children at the desired location. 
from kivy.uix.boxlayout import BoxLayout

#remove these 2 lines 
#import sys
#sys.path.append("/Users/mp/Documents/python/AES/")

from aes.aes import AES
from config import config


# The class whose internal work is in  kv file
class ProgBar(BoxLayout):
    pass


class LoginWindow(Screen):
    bg_color = config.color_background_darker
    bg_button = config.color_background_normal
    plain_text = ObjectProperty(None)
    cipher_text = ObjectProperty(None)
    default_key = config.default_key
    random_key = ""

    def encryptBtn(self):
        master_key = "hychgjuyvhjy"
        aes = AES(master_key)
        
        # check if plain text input is not empty otherwise show error to user
        if(self.plain_text.text != ""):
            # TODO do the Encryption here
            testEnctiption = aes.encrypt(self.plain_text.text)
            MainWindow.current=self.plain_text.text
            #self.ids.cipher_text.text="encrypted"
            self.ids.cipher_text.text = testEnctiption

            print(aes.decrypt(testEnctiption))
            self.reset()
            #sm.current = "main"

        else:
            invalidForm()
       

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.plain_text.text = ""
        #self.cipher_text.text = ""

    def spinner_clicked(self, value):

        if value == "Default":
            self.ids.key_input.disabled = True
            self.ids.key_input.text = config.default_key
        elif value == "User specified":
            self.ids.key_input.disabled = False
            self.ids.key_input.text =  ""
        elif value == "Random":
            self.ids.key_input.disabled = True
            self.ids.key_input.text = config.random_key
        else:
            self.ids.key_input.disabled = False
            self.ids.key_input.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    plain_text = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "encryption"

    def on_enter(self, *args):
        
        self.plain_text.text = "Plain Text: " + self.current
        
        


class WindowManager(ScreenManager):
    pass


def invalidInputs():
    pop = Popup(title='Invalid Input',
                content=Label(text='Invalid input or blank plain text.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in plain text.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("form.kv")

sm = WindowManager()

screens = [LoginWindow(name="encryption"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "encryption"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()

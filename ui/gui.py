from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
# The ProgressBar widget is used to
# visualize the progress of some task
from kivy.uix.progressbar import ProgressBar

# BoxLayout arranges children in a vertical or horizontal box. 
# or help to put the children at the desired location. 
from kivy.uix.boxlayout import BoxLayout

#remove these 2 lines 
#import sys
#sys.path.append("/Users/mp/Documents/python/AES/")
from kivy.uix.textinput import TextInput
import time

from aes.aes import AES
from config import config


# The class whose internal work is in  kv file
from config.config import default_key


class ProgBar(BoxLayout):
    pass


class LoginWindow(Screen):
    bg_color = config.color_background_darker
    bg_button = config.color_background_normal
    plain_text = ObjectProperty(None)
    cipher_text = ObjectProperty(None)
    key_input = ObjectProperty(None)
    default_key = config.default_key
    random_key = ""

    # def next(self, dt):
    #     if (self.ids.progress_bar.value < 100):
    #         self.ids.progress_bar.value += 1
    #     else:
    #         self.ids.cipher_text.text = "encrypted"
    #         # hide progress bar
    #         self.ids.progress_bar.size_hint_y = 0
    #
    # def start(self):
    #     event = Clock.schedule_interval(self.next, 1 / 95)
    #
    # def next(self, dt):
    #     if (self.ids.progress_bar.value < 100):
    #         self.ids.progress_bar.value += 1
    #     else:
    #         self.ids.cipher_text.text = "encrypted"
    #         # hide progress bar
    #         self.ids.progress_bar.size_hint_y = 0
    #
    # def start(self):
    #     event = Clock.schedule_interval(self.next, 1 / 95)

    def encryptBtn(self):
        master_key = default_key

        aes = AES(self.get_user_key())
        # show progress bar
        #self.ids.progress_bar.value = 0
        #self.ids.progress_bar.size_hint_y = 1
        # check if plain text input is not empty otherwise show error to user
        if(self.plain_text.text != ""):
            if(self.ids.encrypt_decrypt_button.text =="Encrypt"):
                # TODO do the Encryption here

                testEnctiption = aes.encrypt(self.plain_text.text)

                MainWindow.current=self.plain_text.text

                self.ids.cipher_text.text = testEnctiption

                self.reset()
                print(testEnctiption);
                #sm.current = "main"
            else:
                # TODO do the Decryption here
                testDecription = aes.decrypt(self.plain_text.text)

                MainWindow.current = self.plain_text.text

                self.ids.cipher_text.text = testDecription

                self.reset()
                print(testDecription);
                # sm.current = "main"
        else:
            invalidForm()

    def changeBtn(self):
        if(self.ids.change_button.text =="Change to decrypt"):
            self.ids.change_button.text = "Change to encrypt"
            self.ids.encrypt_decrypt_button.text = "Decrypt"
            temp = self.ids.label_text_1.text
            self.ids.label_text_1.text = self.ids.label_text_2.text
            self.ids.label_text_2.text = temp
        else:
            self.ids.change_button.text = "Change to decrypt"
            self.ids.encrypt_decrypt_button.text = "Encrypt"
            temp = self.ids.label_text_1.text
            self.ids.label_text_1.text = self.ids.label_text_2.text
            self.ids.label_text_2.text = temp


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

    def get_user_key(self):
        return f"{self.ids.key_input.text}".encode("utf-8").hex()


class MaxLengthInput(TextInput):
    # A class that restricts the input of characters for the key_input field
    max_length = 15  # 16 characters 0-15

    def insert_text(self, substring, from_undo=False):
        if len(self.text) <= self.max_length:
            return super().insert_text(substring, from_undo=from_undo)

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

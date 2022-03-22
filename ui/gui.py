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
from aes.aes import AES
from config import config


# The class whose internal work is in  kv file
class ProgBar(BoxLayout):
    pass


class LoginWindow(Screen):
    bg_color = config.color_background_darker
    bg_button = config.color_background_normal
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    default_key = config.default_key
    random_key = ""

    def loginBtn(self):
        master_key = ""
        aes = AES(master_key)
        """
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
            """

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

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
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        """"
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
        """


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("form.kv")

sm = WindowManager()

screens = [LoginWindow(name="login"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()

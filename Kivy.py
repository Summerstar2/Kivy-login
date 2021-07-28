from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
class LoginScreen(GridLayout):
    def __init__(self,**var_args):
        super(LoginScreen,self).__init__(**var_args)
        self.cols = 2
        self.add_widget(Label(text="Username - "))  
        self.username=TextInput(multiline=True)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password"))
        self.password=TextInput(password=True, multiline=False)
        self.add_widget(self.password)
class MyApp(App):
    def build(self):
        return LoginScreen()
if __name__=="__main__":
    MyApp().run()
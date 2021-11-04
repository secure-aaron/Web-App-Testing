import kivy
from kivy.app import App
from kivy.uix.label import Label # Displays labels
from kivy.uix.gridlayout import GridLayout # Put shit in a grid
from kivy.uix.textinput import TextInput # Allows user input

kivy.require("2.0.0")

class StartPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # Refer to the superclass, which is GridLayout, run the __init__ method such as the one defined on the line above. 
        # This allows us to run this item and the parent at the same time.
        
        
        self.cols = 2 # Create 2 columns
        self.rows = 4 # Create 2 columns

        #self.add_widget(Label(text="topBar!"))
        #self.topBar = TextInput(multiline=False) # create ip object and make it TextInput
        #self.add_widget(self.ip) # Add ip object/TextInput to form.

        self.add_widget(Label(text="IP Address: "))
        self.ip = TextInput(multiline=False) # create ip object and make it TextInput
        self.add_widget(self.ip) # Add ip object/TextInput to form.

        self.add_widget(Label(text="Port: "))
        self.port = TextInput(multiline=False) # create ip object and make it TextInput
        self.add_widget(self.port) # Add ip object/TextInput to form.

        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False) # create ip object and make it TextInput
        self.add_widget(self.username) # Add ip object/TextInput to form.

# Class MyApp inherits App
class MyApp(App):
    def build(self): # Constructor method for this def

        # Instead of just returning a label, we will return a page:
        return StartPage()

        # return Label(text="Hello World!")


if __name__ == '__main__':
    MyApp().run() # Run the app if the name is main



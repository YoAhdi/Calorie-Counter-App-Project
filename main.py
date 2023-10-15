import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AppGrid(GridLayout):
    def __init__(self, **kwargs):
        super(AppGrid, self).__init__(**kwargs)
        self.calories = 0

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Calories input: "))
        self.calorieInput = TextInput(multiline=False)
        self.inside.add_widget(self.calorieInput)

        self.inside.add_widget(Label(text="Total: "))
        self.totalLabel = Label(text=str(self.calories))
        self.inside.add_widget(self.totalLabel)

        self.add_widget(self.inside)

        self.submit = Button(text="Calculate", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.display_button = Button(text="Display Total", font_size=40)
        self.display_button.bind(on_press=self.display_total)
        self.add_widget(self.display_button)

    def pressed(self, instance):
        try:
            calorieInput = int(self.calorieInput.text)
            self.calories += calorieInput
            self.totalLabel.text = str(self.calories)
            self.calorieInput.text = ""
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    def display_total(self, instance):
        self.totalLabel.text = f"Total Calories: {self.calories}"

class MyApp(App):
    def build(self):
        return AppGrid()

if __name__ == "__main__":
    MyApp().run()
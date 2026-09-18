from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=40, spacing=20)

        title = Label(
            text="برنامه من",
            font_size=32
        )

        name = TextInput(
            hint_text="اسمت رو وارد کن",
            multiline=False,
            font_size=22
        )

        button = Button(
            text="ورود",
            font_size=22
        )

        result = Label(
            text="",
            font_size=24
        )

        def welcome(instance):
            result.text = f"سلام {name.text} 👋"

        button.bind(on_press=welcome)

        layout.add_widget(title)
        layout.add_widget(name)
        layout.add_widget(button)
        layout.add_widget(result)

        return layout

MyApp().run()

import webbrowser

from kivy.app import App
from kivy.uix.button import Button


class GreenperpApp(App):
    def build(self):
        button = Button(
            text="Open Greenperp",
            font_size=25
        )

        button.bind(
            on_press=lambda x: webbrowser.open(
                "https://greenperp2.pythonanywhere.com/"
            )
        )

        return button


if __name__ == "__main__":
    GreenperpApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random


class GoalkeeperApp(App):

    def build(self):
        self.target = random.choice(
            ["⬅️ يسار", "➡️ يمين", "⬆️ فوق", "⬇️ تحت"]
        )

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        self.title = Label(
            text="🥅 تدريب حارس المرمى",
            font_size=28
        )

        self.instruction = Label(
            text="استعد!",
            font_size=32
        )

        layout.add_widget(self.title)
        layout.add_widget(self.instruction)

        buttons = BoxLayout(
            orientation="vertical",
            spacing=10
        )

        for text in ["⬆️ فوق", "⬅️ يسار", "➡️ يمين", "⬇️ تحت"]:
            button = Button(
                text=text,
                font_size=25
            )
            button.bind(on_press=self.check_answer)
            buttons.add_widget(button)

        layout.add_widget(buttons)

        self.new_shot()

        return layout

    def new_shot(self):
        self.target = random.choice(
            ["⬅️ يسار", "➡️ يمين", "⬆️ فوق", "⬇️ تحت"]
        )

        self.instruction.text = "🧤 اقفز: " + self.target

    def check_answer(self, button):
        if button.text == self.target:
            self.instruction.text = "✅ تصدي رائع!"
        else:
            self.instruction.text = "❌ الكرة دخلت!"

        Clock.schedule_once(
            lambda dt: self.new_shot(),
            1
        )


if __name__ == "__main__":
    GoalkeeperApp().run()
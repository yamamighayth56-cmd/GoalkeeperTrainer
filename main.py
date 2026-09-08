from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random
import time


class GoalkeeperTrainer(App):

    def build(self):
        self.target = None
        self.start_time = 0

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        self.instruction = Label(
            text="اضغط START للبدء",
            font_size=30
        )

        self.result = Label(
            text="",
            font_size=22
        )

        start = Button(
            text="START",
            font_size=28
        )
        start.bind(on_press=self.start_round)

        layout.add_widget(self.instruction)
        layout.add_widget(self.result)
        layout.add_widget(start)

        return layout

    def start_round(self, instance):
        directions = [
            "يمين",
            "يسار",
            "فوق",
            "أسفل",
            "اندفع يمين",
            "اندفع يسار",
            "تزحلق يمين",
            "تزحلق يسار"
        ]

        self.target = random.choice(directions)
        self.instruction.text = self.target
        self.result.text = "نفّذ الحركة بسرعة!"
        self.start_time = time.time()


GoalkeeperTrainer().run()

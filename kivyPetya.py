from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.label = Label(text='')
        self.texts = ['Hi', 'I\'m Petya', 'Don\'t worry', 'I just break your device', 'and download your confidential data', 'bye:)', '']
        self.current_index = -1
        Clock.schedule_interval(self.next_text, 2)  # Будет вызываться каждую секунду
        return self.label

    def next_text(self, dt):
        self.current_index = (self.current_index + 1) % len(self.texts)  # Зацикливание
        self.label.text = self.texts[self.current_index]
        if self.current_index == 6:
        	exit()

if __name__ == '__main__':
    MyApp().run()
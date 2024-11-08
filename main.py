from kivy.app import App #App - основной класс для создания приложений на киви
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (360, 640)

class Container(GridLayout):
    # def calculate(self, *args):
    #     try:
    #         calc_entry = self.label.text
    #         ans = str(eval(calc_entry))
    #         self.label.text = ans
    #     except Exception:
    #         self.label.text = "Error!"
    #         pass
    #
    # def drop(self, *args):
    #     self.label.text = ""

    first_number = 0
    action = ''

    def set_number(self, number):
        if number == 0 and self.label.text == "":
            return
        self.label.text = self.label.text + str(number)

    def set_point(self):
        if len(self.label.text.split('.'))>1:
            return
        if self.label.text == '':
            self.label.text = '0.'
        else:
            self.label.text = self.label.text + '.'

    def clear_all(self):
        self.label.text = ''

    def calculate(self, action):
        self.first_number = float(self.label.text)
        self.action = action
        self.label.text = ''

    def result(self):
        res = ''
        if self.action == '+':
            res = self.first_number + float(self.label.text)
        elif self.action == '-':
            res = self.first_number - float(self.label.text)
        elif self.action == '*':
            res = self.first_number * float(self.label.text)
        elif self.action == "/":
            res = self.first_number / float(self.label.text)

        self.label.text = str(res)
        self.first_number = 0
        self.action = ''


class CalckApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    CalckApp().run()


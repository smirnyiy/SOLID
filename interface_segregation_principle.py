# Добавим класс Notification, который предоставляет интерфейс для использования в конкретных классах
# Добавляем его как абстракцию, которая предоставляет требуемый интерфейс или метод .getText().
class Notification:
    def getText(self):
        pass

class Text(Notification):
    def __init__(self, text):
        self.text = text

    def getText(self):
        return self.text


class Printer:
    def print(self, text):
        print(text.getText())


if __name__ == "__main__":
    myText = Text("Hello, world!")
    myPrinter = Printer()
    myPrinter.print(myText)

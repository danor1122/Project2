class Widget:
    def __init__(self, label):
        self.label = label

# w = Widget('my widget')
# print(w.label)
# b = Button('my button')

class Button(Widget): # klasa buttom ktora dziedziczy z klasy Widget, 
    # ma dostep do wszystkiego co jest w klasie Widget
    # pass
    def __init__(self, label, size):
        super().__init__(label) # za pomoca super odwolujemy sie do instancji label z klasy Widget i przypisujemy label
        self.size = size

    def handle_click(self): # dostepny tylko dla klasy przycisku, klasa Widget(na gorze, nie ma dostepu do klas dziedziczacych )
        return 'Click!'

b = Button('my button', 'large')
print(b.label, b.size)

print(b.handle_click())

w = Widget('my widget')
# w.handle_click()  # jak widac klasa bazowa nie ma dostepu do klasy Button
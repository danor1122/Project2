import pylab
import numpy as np
import matplotlib.pyplot as plt


# x = [1,2,3]
# y = [4,6,5]
# pylab.plot(x,y)
# pylab.show()

a = int(input("Type value a:"))
b = int(input("Type value b: "))
x = range(-10, 11)  # lista argumentów x

y = []  # lista wartości
for i in x:
    y.append(a * i + b)

pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x - b') #  tytul wykresu
pylab.grid(True) #  włącza kratke
pylab.show()  # pokazuje wykres
class Point:
#     def __init__(self): # bez definiowania x i y przyjmuje 0, 0
#         self.x = 0
#         self.y = 0

# p1 =Point()
# print(p1.x, p1.y) 
    # zbior wszystkich punktów mogłby byc atrybutem calej klasy
    # 
    # atrybuty instancji
    points_counter = 0


    def __init__(self, x=0, y=0):  # x=0, jesli nie podano, przyjmuje domyslnie wartosc 0
        self.x = x
        self.y = y
        Point.points_counter += 1

    def move_to_now_coords(self, x=0, y=0):
        self.x = x
        self.y = y
    # w klasie tworzymy metody do obiektow
            
p1 = Point(3, 4)
print(p1.x, p1.y)
p1.x = 7
p1.y = 17
print(p1.x, p1.y)
p1.move_to_now_coords(12,4)
print(p1.x, p1.y)

p2 = Point(1, 5)

# klasy a instancje
p1.points_counter = 12 # uzyty na rzecz instancji klasy
Point.points_counter = 2 #uzyty na rzecz klasy
print(p1.points_counter)
print(Point.points_counter)

print(Point.points_counter, "Point counter")
print(p2.points_counter) # Wszystkie punkty dziedziczą instancje point counter
# [Андрей Гурьянов]

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

print('\n\nЗадача 1\n')

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def tr_area(self):
        # Площадь треугольника
        return float(abs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1))/2)

    @property
    def tr_sides(self):
        # Вычисление сторон треугольника
        ab = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        bc = math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        ac = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
        return ab, bc, ac


    def tr_hights(self, ab, bc, ac):
        # Высота треугольника
        # Сделал только для высоты опущенной из вершины x2,y2.
        # Для остальных вершин можно сделать копией
        p = (ab + bc + ac) / 2
        h1 = math.sqrt(p * (p - ab) * (p - bc) * (p - ac)) * 2 / ab
        h2 = math.sqrt(p * (p - ab) * (p - bc) * (p - ac)) * 2 / bc
        h3 = math.sqrt(p * (p - ab) * (p - bc) * (p - ac)) * 2 / ac
        return h1, h2, h3 

    def tr_perimeter(self, ab, bc, ac):
        # Периметр треугольника.
        return ab + bc + ac


Triangle_1 = Triangle(23, 16, -23, 34, -22, 18)
print('Площадь треугольника: ', Triangle_1.tr_area())
print('Дины сторон треугольника: ', Triangle_1.tr_sides)
print('Высоты треугольника: ', Triangle_1.tr_hights(Triangle_1.tr_sides[0], Triangle_1.tr_sides[1], Triangle_1.tr_sides[2]))
print('Периметр треугольника: ', Triangle_1.tr_perimeter(Triangle_1.tr_sides[0], Triangle_1.tr_sides[1], Triangle_1.tr_sides[2]))




# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print('\n\nЗадача 2\n')

class Trapezoid:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    @property
    def trap_sides(self):
        # Вычисление сторон трапеции
        ab = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        bc = math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        cd = math.sqrt((self.x3 - self.x4) ** 2 + (self.y3 - self.y4) ** 2)
        ad = math.sqrt((self.x1 - self.x4) ** 2 + (self.y1 - self.y4) ** 2)
        return ab, bc, cd, ad

    def trap_equal(self, ab, bc, cd, ad):
        if (ab == cd) or (bc == ad):
            return True
        else:
            return False

    def trap_perimeter(self, ab, bc, cd, ad):
        # Периметр трапеции.
        return ab + bc + cd + ad

    def trap_area(self, ab, bc, cd, ad):
        if ab == cd:
            return ((bc + ad) / 2) * math.sqrt(ab ** 2 - ((bc - ad) ** 2 / (2 * (bc - ad))) ** 2)
        else:
            return ((ab + cd) / 2) * math.sqrt(bc ** 2 - ((ab - cd) ** 2 / (2 * (ab - cd))) ** 2)
    
    
    
Trapezoid_1 = Trapezoid(-6, 0, 6, 0, 2, 2, -2, 2)
print('Дины сторон трапеции: ', Trapezoid_1.trap_sides)
if Trapezoid_1.trap_equal(Trapezoid_1.trap_sides[0], Trapezoid_1.trap_sides[1],\
                          Trapezoid_1.trap_sides[2], Trapezoid_1.trap_sides[3]):
    print('Трапеция равнобокая')
else:
    print('Трапеция не равнобокая')
print('Периметр трапеции: ', Trapezoid_1.trap_perimeter(Trapezoid_1.trap_sides[0], \
                                                        Trapezoid_1.trap_sides[1], \
                                                        Trapezoid_1.trap_sides[2], \
                                                        Trapezoid_1.trap_sides[3]))
print('Площадь трапеции: ', Trapezoid_1.trap_area(Trapezoid_1.trap_sides[0], \
                                                  Trapezoid_1.trap_sides[1], \
                                                  Trapezoid_1.trap_sides[2], \
                                                  Trapezoid_1.trap_sides[3]))

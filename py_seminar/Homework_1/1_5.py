#Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

 

import math
import sys

firstCoord = (input('Введите координаты перрвой координаты через пробел: ').split())
(ax,ay) = list(map(int, firstCoord))

secondCoord = (input('Введите координаты второй точки через пробел: ').split())
(bx,by) = list(map(int, secondCoord))

ll = math.sqrt((bx - ax)**2 + (by - ay)**2)
#print(f'{ll}')
print("%.3f" % ll)
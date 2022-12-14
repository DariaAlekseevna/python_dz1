# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x_1 = int(input('введите координату точки А по Х: '))
y_1 = int(input('введите координату точки А по Y: '))
x_2 = int(input('введите координату точки B по Х: '))
y_2 = int(input('введите координату точки B по Y: '))

distance = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5
print(f'расстояние между А и В в 2D пространстве = {round(distance, 2)}')
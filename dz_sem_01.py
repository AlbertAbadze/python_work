# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
 
# day = int(input('введите день недели: '))
# if day > 7 or day < 1:
#     print('Введите корректктную цифру')
# elif day == 6 or day == 7:
#     print('Да, выходной')
# else:
#     print('Нет, надо на работу')
# print()


# 2. Напишите программу для. 
# Проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

# result = True
# for x in 1, 0:
#     for y in 1, 0:
#         for z in 1, 0:
#             print(f"{x = } {y = } {z = }  {not(x or y or z) == (not x and not y and not z)}")


# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# x=int(input('Введите ко - x: '))
# y=int(input('Введите ко - y: '))

# if  x > 0 and y > 0:
#     print(f'Точка({x}, {y}) расположена в первой четверти')
# elif x < 0 and y > 0:
#     print(f'Точка({x}, {y}) расположена во второй четверти')    
# elif x < 0 and y < 0:
#     print(f'Точка({x}, {y}) расположена в третей четверти ')    
# elif x > 0 and y < 0:
#     print(f'Точка({x}, {y}) расположена в четвертой четверти')  
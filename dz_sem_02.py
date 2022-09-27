# 1. Напишите программу, которая принимает на вход вещественное 
# или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number


# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum


# num = InputNumbers("Введите число: ")

# print(f"Сумма цифр = {sumNums(num)}")

# 2. Напишите программу, которая принимает 
# на вход число N и выдает набор произведений чисел от 1 до N.

# def factorial (number, count = 1):
#     for i in range(1, number + 1):
#         count *= i
#     return count

# n = int(input('Enter the number: '))
# print(f'Set of products of numbers from 1 to {n} = ', end = '')
# for i in range(1, n + 1):
#     if i == n: 
#         print(f'{factorial(i)}')
#     else:
#         print(f'{factorial(i)}', end = ', ')

# 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, выводится на экран,
# затем перемешивается, опять выводится на экран
# from random import random

# import random
# lst = [random.randint(0,10) 
# for i in range(random.randint(5,20))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")


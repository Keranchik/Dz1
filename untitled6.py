# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QlCp3DAu8glLicgxukC2ZjrDOXVTu0zE
"""

1) number = 123
sum = 0

while number > 0:
    digit = number % 10
    sum += digit
    number //= 10

print("Сумма цифр числа:", sum)

2) n = int(input())
if n > 2:
   for i in range(1, n - 2):
       summ = (n - 1)
   print(i * (n * summ))
elif n == 0 or n == 1:
    print("1")

3) for i in range(101):
    if i%9==0 or i==range(9,99,10):
        print(i)
# Author: MOG 1/18/22

first = int(input("Input your first number: "))
second = int(input("Input your second number: "))

def sum_nums(num1, num2):
    if num1 == num2:
        print(num1)
    else:
        print(num1 + num2)

sum_nums(first, second)
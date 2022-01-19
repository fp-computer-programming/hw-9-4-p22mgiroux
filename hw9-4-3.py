# Author: MOG 1/18/22

input = input("Please input a string: ")

def count_e(string):
    number_of_e = string.lower().count("e")
    print(number_of_e)

count_e(input)
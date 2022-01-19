# Author: MOG 1/18/22

numbers = [2,35,45,68,53,43,46,34,12,5,6,3]
value = 5

def products(lst, val):
    final_nums = []
    for num in lst:
        final_nums += [num * val]
    print(final_nums)
    
products(numbers, value)
print(" This is a functional module for AI project. ")

table = [5] * 10
print(table)


def draw_cat():
    cat = r"""
 /\_/\  
( o.o ) 
 > ^ <  
"""
    print(cat)

draw_cat()

import random
table = [random.randint(0, 99) for _ in range(10)]
print(table)
table.sort()
print(table)
table.reverse()
print(table)



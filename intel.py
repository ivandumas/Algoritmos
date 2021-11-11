#input: num
#func: factorial
#output res

import sys

def factorial(num):
    aux = 1
    res =  1
    for i in range(num,0,-1):
        res *= i
    return res

print(factorial(0))

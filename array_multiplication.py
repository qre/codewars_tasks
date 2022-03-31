#my solution:
import math
def grow(arr):
    result = math.prod(arr)
    return result

#best voted solutions:
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product

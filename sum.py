def summation(num):
    su = 0
    for i in range(1, num+1):
        su += i
    return su

def summation(num):
    return sum(range(num + 1))

# In Python 2.x:

# range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.

# xrange is a sequence object that evaluates lazily.

# In Python 3:

# range does the equivalent of Python 2's xrange. To get the list, you have to explicitly use list(range(...)).
# xrange no longer exists.
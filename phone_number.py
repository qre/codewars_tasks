n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#my solution:
def mapz(n):
    m = ''.join(map(str,n))
    print(m)
    return m
mapz(n)
def create_phone_number_mine(n):
    re = f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
    print(re)
    return re

#best voted solutions:
def create_phone_number(n):
    m = ''.join(map(str, n))
    m = f"({n[:3]}) {n[3:6]}-{n[6:]}"
    print(m)
    return m

def create_phone_number1(n):
    e = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    print(e)
    return e

def create_phone_number2(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
#create_phone_number1(n)
#print(n)

number = 25
def even_or_odd(number):
    x = abs(number) / 2
    print(x)
    if x is int:
        return 'Even'
    elif x is float: 
        return 'Odd'
even_or_odd(number)
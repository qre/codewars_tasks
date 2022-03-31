num = 9119
def square_digits(num):
    result = ''
    for i in str(num):
        result += str(int(i)**2)
    print(int(result))
    return int(result)
square_digits(num)
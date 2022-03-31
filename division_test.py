#my solution:
def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False

    #best voted solution:
def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0

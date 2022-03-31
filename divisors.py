def divisors(integer):
    arr = []
    for i in str(integer):
        if i // integer:
            arr += i
        if len(i // integer) ==0:
            return ([i].join('is a prime number!'))
    return arr
wrong

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n

def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

def divisors(integer):
  a = []
  for i in range(2, integer):
    if integer % i == 0:
      a.append(i)
  return a if a else str(integer) + " is prime"



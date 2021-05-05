import math
a = 3
b = 16


def isPrime(num):
    if num ==1:
        return False

    n = int(math.sqrt(num)) #제곱근까지만 비교해보면 된다
    for i in range(2, n+1):
        if num % i==0:
            return False
    return True


for i in range(a, b + 1):
    if isPrime(i):
        print(i)

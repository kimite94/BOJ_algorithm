import math

def isPrime(num):
    if num ==1:
        return False

    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i==0:
            return False
    return True

a_list = list(range(2,10001))
s_list = []
for i in a_list:
    if isPrime(i):
        s_list.append(i)
3
n1 = int(input())
for i in range(n1):
    t = int(input())
    m = t//2
    while True:
        if m in s_list and t-m in s_list:
            print(m,t-m)
            break
        else:
            m -=1
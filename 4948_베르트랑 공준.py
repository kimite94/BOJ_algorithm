import math

def isPrime(num):           # 소수를 구하는 함수
    if num ==1:
        return False

    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i==0:
            return False
    return True

a_list = list(range(2,123456*2))   #범위에 있는 숫자 중 소수를 먼저 모두 구한다
s_list = []
for i in a_list:
    if isPrime(i):
        s_list.append(i)

while True:
    a = int(input())
    sum1 = 0
    if a ==0:
        break
    for i in s_list:
        if a<i<=2*a:            # 값에 맞는 범위에 있는 소수의 개수를 구한다.
            sum1 +=1
    print(sum1)

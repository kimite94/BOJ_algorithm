n = int(input())

def sum_digit(number):
    return sum(map(int,str(number)))

for i in range(1,n+1):
    sum1 = 0
    sum2 = sum_digit(i)
    sum1 = i+sum2
    if sum1 ==n:
        print(i)
        break
    if i == n:
        print(0)


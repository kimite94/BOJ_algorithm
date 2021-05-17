n = int(input())

for i in range(n):
    m = int(input())
    zero = 1
    one = 0
    number = 0
    for _ in range(m):
        number = one
        one = one + zero
        zero = number
    print(zero, one)



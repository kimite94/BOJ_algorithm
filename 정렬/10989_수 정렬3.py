import sys
n = int(sys.stdin.readline())
a_list = [0]*10001     # 0에서 10000까지 들어올 수 있는 자연수 0으로 일단 초기화

for i in range(0,n):
    num = int(sys.stdin.readline())
    a_list[num] += 1

for i in range(0,10001):
    if a_list[i] != 0:
        for j in range(0,a_list[i]):
            print(i)


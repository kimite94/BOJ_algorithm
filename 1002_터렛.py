import math

n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)     # 두 중심 사이의 거리


    if dis ==0 and r1==r2:               # 두 중심의 좌표가 같을 때(원의 크기가 같거나 다른 경우)
        print(-1)
    elif abs(r1-r2) == dis or r1+r2 == dis:
        print(1)
    elif abs(r1-r2) < dis < (r1+r2):
        print(2)
    else:
        print(0)
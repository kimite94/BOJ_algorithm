from itertools import combinations

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
sum1 = 0

for i in combinations(a_list,3):    #조합 사용
    sum2 = sum(i)
    if sum1 < sum2 <= m:
        sum1 = sum2
print(sum1)


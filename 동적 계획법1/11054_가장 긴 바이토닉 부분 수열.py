n = int(input())

arr = list(map(int, input().split()))

a_list = [1 for i in range(n)]
b_list = [1 for i in range(n)]
result = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            a_list[i] = max(a_list[i], a_list[j]+1)

for i in range(n-1,-1,-1):          # 감소하는 수열
    for j in range(n-1,i,-1):
        if arr[i] > arr[j]:
            b_list[i] = max(b_list[i], b_list[j]+1)

    result[i] = a_list[i] + b_list[i]-1

print(max(result))

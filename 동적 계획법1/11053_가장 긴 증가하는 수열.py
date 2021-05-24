n = int(input())

arr = list(map(int, input().split()))
a_list = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            a_list[i] = max(a_list[i], a_list[j]+1)

print(max(a_list))
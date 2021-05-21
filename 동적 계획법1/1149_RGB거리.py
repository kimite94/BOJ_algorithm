n = int(input())
a_list = []
for i in range(n):
    a_list.append(list(map(int, input().split())))

for i in range(1,n):
    a_list[i][0] = min(a_list[i-1][1],a_list[i-1][2])+a_list[i][0]
    a_list[i][1] = min(a_list[i - 1][0], a_list[i - 1][2]) + a_list[i][1]
    a_list[i][2] = min(a_list[i - 1][1], a_list[i - 1][0]) + a_list[i][2]

print(min(a_list[n-1]))




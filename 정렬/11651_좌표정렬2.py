n = int(input())
a_list = []
for i in range(0,n):
    [x,y] = map(int, input().split())
    a_list.append([x,y])

a_list.sort(key = lambda x : (x[1],x[0]))

for i in range(0,n):
    print(a_list[i][0],a_list[i][1])


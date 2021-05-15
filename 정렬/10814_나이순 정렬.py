n = int(input())
a_list = []
for i in range(0,n):
    x,y = map(str, input().split())
    x = int(x)
    a_list.append([x,y])

a_list.sort(key = lambda x : (x[0]))

for i in a_list:
    print(i[0], i[1])

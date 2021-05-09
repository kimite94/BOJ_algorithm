n = int(input())
a_list = []

for i in range(0,n):
    x,y = map(int,input().split())
    a_list.append((x,y))

for i in a_list:
    rank = 1
    for j in a_list:
        if i[0]<j[0] and i[1]<j[1]:
            rank +=1
    print(rank, end =" ")

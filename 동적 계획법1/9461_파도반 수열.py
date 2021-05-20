n = int(input())

a_list = [i for i in range(101)]
a_list[1]=1
a_list[2]=1
a_list[3]=1
for i in range(4,101):
    a_list[i] = a_list[i-2] + a_list[i-3]

for i in range(n):
    m = int(input())
    print(a_list[m])



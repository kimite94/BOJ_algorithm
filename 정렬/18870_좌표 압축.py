n = int(input())
a_list = list(map(int, input().split()))

a_set = list(set(a_list))
a_set.sort()

dic = {v:i for i,v in enumerate(a_set)}
print(dic)
for i in a_list:
    print(dic[i], end = ' ')


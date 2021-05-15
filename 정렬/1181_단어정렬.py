n = int(input())
a_list = []
for i in range(0,n):
    a = str(input())
    a_list.append(a)

a_list = list(set(a_list))
a_list.sort(key = lambda x : (len(x),x))

for i in range(0,len(a_list)):
     print(a_list[i])
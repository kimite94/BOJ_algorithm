n = int(input())
m = str(n)
a_list = []
for i in m:
    a_list.append(i)
a_list.sort()
a_list.reverse()
for i in a_list:
    print(i, end = "")

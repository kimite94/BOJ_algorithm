n = int(input())
a_list = [0]*1000001
a_list[1] = 1
a_list[2] = 2

for i in range(3, n+1):
    a_list[i] = (a_list[i-2]+a_list[i-1])%15746

print(a_list[n])


# import itertools
# n = int(input())
# # a_list = []
# m = n//2
# cnt = 0
# for i in range(0,m+1):
#     a_list = []
#     for j in range(0,(n-2*i)+i):
#          a_list.append(j)
#     cnt += len(list(itertools.combinations(a_list, i)))
#
# print(cnt)
import math

while True:
    a_list = list(map(int, input().split()))
    if sum(a_list) == 0:
        break
    max_num = max(a_list)
    a_list.remove(max_num)
    if (a_list[0]**2)+(a_list[1]**2) == max_num**2:
        print("right")
    else:
        print("wrong")


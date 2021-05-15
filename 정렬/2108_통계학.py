import sys
from collections import Counter
# counter: 각 요소별 갯수 count해서 dictionary
def mean(num):
    return round(sum(num)/n)

def median(num):
    if n ==1:
        return num[0]
    else:
        return num [n // 2]

def most(num):
    b_list = []
    if n ==1:
        return num[0]
    else:
        counter = Counter(num)
        cnt = counter.most_common(2)        # 리스트내 최빈값 꺼내기(most_common)
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]

def range_(num):
    if n ==1:
        return 0
    else:
        return a_list[-1] - a_list[0]

n = int(sys.stdin.readline())
a_list = []
for _ in range(n):
    a_list.append(int(sys.stdin.readline()))
a_list.sort()


print(mean(a_list))
print(median(a_list))
print(most(a_list))
print(range_(a_list))


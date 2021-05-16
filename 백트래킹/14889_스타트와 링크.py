import itertools
n = int(input())
a_list = []
for i in range(n):
	a_list.append(i)
team = list(itertools.combinations(a_list, int(n/2)))           # 조합
for i in range(n):
    a_list[i] = list(map(int, input().split()))

min_score = 100*100
for team_start in team:
    start = 0
    link = 0
    for x in team_start:
        for y in team_start:
            start += a_list[x][y]
    j = []
    for a in range(n):
        if a not in team_start:
            j.append(a)
    for x in j:
        for y in j:
            link += a_list[x][y]
    if abs(start-link) < min_score:
        min_score = abs(start-link)

print(min_score)
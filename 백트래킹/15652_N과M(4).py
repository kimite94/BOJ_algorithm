n, m = map(int, input().split())


a_list = []
def f(num):
    if len(a_list) == m:
        print(' '.join(map(str, a_list)))
        return
    for i in range(num, n + 1):
        a_list.append(i)
        f(i)
        a_list.pop()


f(1)
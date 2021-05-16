n, m = map(int, input().split())
# 중복허용 금지

a_list = []
def f(num):
    if len(a_list) == m:
        print(' '.join(map(str, a_list)))
        return
    for i in range(num, n + 1):         # 첫 숫자보다 작은 숫자는 for문에서 제외
        if i not in a_list:
            a_list.append(i)
            f(i+1)                      # 처음 들어있는 숫자보다 큰 숫자 대입
            a_list.pop()


f(1)
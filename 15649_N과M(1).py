n, m = map(int, input().split())

def f(s):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    f(s + [i])      #처음에 f[1], f[2], f[3], f[4]를 쏟아내고, 이후에 앞에 것들이 숫자를 하나씩 찾아옴

f([])
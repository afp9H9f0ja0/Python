n = 7

a = [[max(0, n - i - j) for j in range(n)] for i in range(n)]

for r in a:
    print(*r)
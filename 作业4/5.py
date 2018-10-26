def fun(x, t):
    l = []
    while x:
        r = x % t
        x //= t
        l.append(r)
    ans = ''
    for i in l:
        ans = ans + str(i)
    return ans


B = int(input())
L = []
for n in range(1, 301):
    k = n * n
    p = fun(k, B)
    if p == p[::-1]:
        L.append(n)
for each in L:
    print(each, end=' ')
    print(each**2, end=' ')
    print(fun(each**2, B))

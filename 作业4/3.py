def sor(L):    # sort L in bubble
    n = len(L)
    for j in range(0, n-1):
        for i in range(0, n-1-j):
            if L[i][0] > L[i+1][0]:
                L[i], L[i+1] = L[i+1], L[i]
    return L


def fun(k):  # k is a list
    end = 0
    star = 0
    L = []      # a list to store the continuous time
    for i in range(1, len(k)):
        if k[i][0] < k[end][1] < k[i][1]:
            end = i
        elif k[i][0] > k[end][1]:
            L.append([k[star][0], k[end][1]])
            end = i
            star = i
    L.append([k[star][0], k[end][1]])
    return L


def time_in(L):     # the longest time that have at least one person working
    n = []
    for i in L:
        n.append(i[1]-i[0])
    x = max(n)
    return x


def time_out(L):    # the longest time that has nobody working
    n = []
    for i in range(1, len(L)):
        n.append(L[i][0] - L[i-1][1])
    x = max(n)
    return x


P = [[300, 1000], [700, 1200], [1500, 2100]]
s = fun(sor(P))     # the s has been sorted
print(time_in(s), end=' ')
print(time_out(s))

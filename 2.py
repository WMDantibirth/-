def fun1(a):
    x = int(a)
    r = 0
    Rs = []
    while x:
        r = x % 2
        x //= 2
        Rs = [r] + Rs
    ans = ''
    for i in range(len(Rs)):
        ans = ans + str(Rs[i])
    return ans


def fun2(a):
    a = float('0.' + a)
    k = ''
    while len(k) <= 8 and a != 0:
        if a >= 0.5:
            k = k + '1'
            a -= 0.5
        else:
            k = k + '0'
    return k


b = input()
try:
    int(b)
except ValueError:
    x, y = b.split('.')
    x = fun1(x)
    y = fun2(y)
    print(x+'.'+y)
else:
    b = str(b)
    print(fun1(b))

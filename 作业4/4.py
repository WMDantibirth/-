'''
L = list(input())
a = L[0][0]
b = L[0][1]
for i in range(1, len(L)):
    if L[i][0] <= L[i-1][1]:
'''
def fun(k):
    max=0
    star=0
    s=[]
    for i in range(1,len(k)):
        if k[i][1]>k[max][1] and k[i][0]<=k[max][1]:
            max=i
        elif k[i][0]>k[max][1]:
            s.append([k[star][0],k[max][1]])
            max=i
            star=i
        if i==len(k)-1:
            s.append([k[star][0],k[max][1]])
    return s 


L = [[300,1000],[700,1200],[1500,2100]]
s=fun(L)
print(s)
xx=0
m=0
for j in range(1,len(s)):
    n=s[m][1]-s[m][0]
    b=s[j][1]-s[j][0]
    if b>n:
        m=j
print("至少一人",s[m])  
for i in range(1,len(s)):
    g=s[xx][0]-s[xx][1]
    c=s[i][0]-s[i-1][1]
    if c>g:
        xx=i
print("无人时段",[s[xx-1][1],s[xx][0]])



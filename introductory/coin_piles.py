a=int(input().strip())
sol=[]
for i in range(a):
    b,c=map(int,input().strip().split())
    if c>b:
        b,c=c,b
    if b>2*c or (b+c)%3!=0:
        sol.append("NO")
    else:
        sol.append("YES")
for i in sol:
    print(i)
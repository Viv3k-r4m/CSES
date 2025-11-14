a=int(input().strip())
b=list(map(int,input().strip().split()))
c=float("-inf")
d=0
for i in b:
    d=max(i,d+i)
    c=max(c,d)
print(c)

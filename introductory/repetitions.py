b=input().strip()
c=1
d=0
for i in range(len(b)-1):
    if b[i]==b[i+1]:
        c+=1
    else:
        d=max(d,c)
        c=1
d=max(d,c)
print(d)

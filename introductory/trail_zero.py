import math
a=int(input().strip())
i=1
s=0
while(True):
    res=math.floor(a/pow(5,i))
    if res==0:
        break
    s+=res
    i+=1
print(s)
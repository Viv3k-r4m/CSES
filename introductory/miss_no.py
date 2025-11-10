a=int(input().strip())
b=list(map(int,input().strip().split()))
b.sort()
for i in range(a-1):
    if b[i]!=i+1:
        print(i+1)
        break
else:
    print(a)

def hanoi(n,a1,a3,a2):
    if n==0:
        return
    hanoi(n-1,a1,a2,a3)
    print(a1,a3)
    hanoi(n-1,a2,a3,a1)

a=int(input().strip())
print(2**a-1)
hanoi(a,1,3,2)#from,to,aux
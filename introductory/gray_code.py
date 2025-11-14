n=int(input().strip())
for i in range(1 << n):
    print(format(i ^ (i >> 1), f'0{n}b'))

#f0nb->0 for padding zeroes to length n,b for binary

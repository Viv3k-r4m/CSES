n, x = map(int, input().split())
a = list(map(int, input().split()))
arr = [(a[i], i + 1) for i in range(n)]
arr.sort()

l, r = 0, n - 1
while l < r:
    s = arr[l][0] + arr[r][0]
    if s == x:
        print(arr[l][1], arr[r][1])
        break
    elif s < x:
        l += 1
    else:
        r -= 1
else:
    print("IMPOSSIBLE")

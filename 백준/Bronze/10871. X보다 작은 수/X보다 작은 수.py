a, n = map(int, input().split())
lst = list(map(int, input().split()))

for i in lst:
    if n > i:
        print(i, end=' ')
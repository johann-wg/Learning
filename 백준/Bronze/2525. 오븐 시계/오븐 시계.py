hour = list(map(int, input().split()))
h = hour[0]
m = hour[1]
o = int(input())
h +=(o+m) // 60
m = (m + o - 60) % 60
if h >= 24:
    h = h % 24
print(h, m)
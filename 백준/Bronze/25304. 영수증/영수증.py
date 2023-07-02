total = int(input())
total_count = int(input())
total_price = 0
for _ in range(1, total_count+1):
    a, b = list(map(int, input().split()))
    total_price += a * b
if total == total_price:
    print('Yes')
else:
    print('No')
import sys

count = sys.stdin.readline().rstrip()
count = int(count)

for i in range(count):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{i + 1}: {a+b}')
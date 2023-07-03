import sys

count = sys.stdin.readline().rstrip()
count = int(count)
for _ in range(count):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)
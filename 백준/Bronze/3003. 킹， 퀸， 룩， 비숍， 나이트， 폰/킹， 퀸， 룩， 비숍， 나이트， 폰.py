num = list(map(int, input().split()))

for i in range(len(num)):
    if i <= 1:
        print(1 - num[i], end=' ')
    elif 1 < i < 5:
        print(2 - num[i], end=' ')
    elif i == 5:
        print(8 - num[i], end=' ')
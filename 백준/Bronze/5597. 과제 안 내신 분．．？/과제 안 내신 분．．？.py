num = []
answer = []
for _ in range(1, 29):
    num.append(int(input()))
for i in range(1, 31):
    if i not in num:
        answer.append(i)
print(min(answer))
print(max(answer))
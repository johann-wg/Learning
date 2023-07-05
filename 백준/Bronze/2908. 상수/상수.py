lst = list(input().split())
answer = []
for c in lst:
    answer.append(c[::-1])
print(max(answer))
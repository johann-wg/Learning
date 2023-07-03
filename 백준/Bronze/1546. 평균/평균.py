a = int(input())
score = list(map(int, input().split()))
answer = 0
for i in score:
    answer += (i / max(score) * 100)
print(answer/a)
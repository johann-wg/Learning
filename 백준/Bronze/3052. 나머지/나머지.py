answer = []
count = 0
for _ in range(10):
    num = int(input())
    if num % 42 not in answer:
        answer.append(num % 42)
        count += 1
print(count)
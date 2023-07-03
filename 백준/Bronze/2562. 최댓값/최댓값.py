top = 0
count = 0
for i in range(9):
    num = int(input())
    if num > top:
        top = num
        count = i+1
print(top)
print(count)
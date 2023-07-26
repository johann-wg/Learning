lst = []
for _ in range(9):
    lst.append(list(map(int, input().split())))

max_num = 0
idx = 0
for n, i in enumerate(lst):
    if max(i) > max_num:
        max_num = max(i)
        idx = n
print(max_num)
print(idx+1, lst[idx].index(max_num)+1)
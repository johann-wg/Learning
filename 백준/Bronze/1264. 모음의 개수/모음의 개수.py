char = input().lower()
lst = ['a','e','i','o','u']
answer = 0
while char != '#':
    for c in lst:
        answer += char.count(c)
    print(answer)
    answer = 0    
    char = input().lower()

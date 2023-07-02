char = input().upper()
count = 0
top = 0
lst = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
answer = ''
for i in lst:
    count = (char.count(i))
    if count > top:
        top = count
        answer = i
    elif count == top:
        answer = '?' 

print(answer)
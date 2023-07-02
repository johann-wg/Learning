a = str(input())
b = a[::-1]
while a != '0':
    if a == b:
        print('yes')
    elif a != b:
        print('no')
    a = str(input())
    b = a[::-1]
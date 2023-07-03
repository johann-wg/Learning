a, b, c = map(int, input().split()) 
lst = [a,b,c]

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == a or b == c:
    print(1000 + b * 100)
elif c == a or c == b:
    print(1000 + c * 100)
elif a != b != c:
    print(max(lst) * 100)
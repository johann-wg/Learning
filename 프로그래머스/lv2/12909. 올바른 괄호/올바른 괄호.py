def solution(s):
    lst = []
    for c in s:
        if c == '(':
            lst.append(c)
        elif c == ')':
            if not lst:
                return False
            lst.pop()
    if len(lst) == 0:
        return True
    else:
        return False
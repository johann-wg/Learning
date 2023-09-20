def solution(t, p):
    answer = 0
    tmp = []
    for i in range(0, len(t)):
        if len(t[i:i+len(p)]) < len(p):
            pass
        else:
            tmp.append(int(t[i:i+len(p)]))

    for j in tmp:
        if j <= int(p):
            answer += 1
    return answer
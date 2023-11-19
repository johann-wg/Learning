def solution(n):
    answer = 0
    standard = bin(n)[2:].count('1')
    for i in range(n+1, 1000000):
        if bin(int(i))[2:].count('1') == standard:
            answer = i
            break
    return answer

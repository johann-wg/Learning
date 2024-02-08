def solution(rny_string):
    answer = ''
    for c in rny_string:
        if c == 'm':
            answer += 'rn'
        else:
            answer += c
    return answer
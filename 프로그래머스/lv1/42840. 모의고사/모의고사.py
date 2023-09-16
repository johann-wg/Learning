def solution(answers):
    answer = []
    score = []
    a_count = 0
    b_count = 0
    c_count = 0
    a = [1,2,3,4,5] * len(answers)
    b = [2,1,2,3,2,4,2,5] * len(answers)
    c = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    for idx, i in enumerate(answers):
        if a[idx] == i:
            a_count += 1
        if b[idx] == i:
            b_count += 1
        if c[idx] == i:
            c_count += 1
        else:
            pass
    score = [a_count, b_count, c_count]
    top = max(score)
    answer = [idx2+1 for idx2,l in enumerate(score) if l == top]
        
    return answer
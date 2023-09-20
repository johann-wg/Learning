def solution(arr):
    answer = []
    for i in arr:
        if answer == []:
            answer.append(i)
        else: 
            if answer[-1] != i:
                answer.append(i)
    return answer
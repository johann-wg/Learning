def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = array[commands[i][0]-1:commands[i][1]]
        temp.sort()
        temp = temp[commands[i][2]-1]
        answer.append(temp)

    return answer
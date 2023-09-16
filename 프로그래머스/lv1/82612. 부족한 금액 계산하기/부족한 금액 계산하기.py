def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        money -= price * i
        if money < 0:
            answer = abs(money)
        elif money <= price:
            answer = 0
        else:
            answer = -1
    return answer
#메뉴만 적은 경우 -> 차가운 것
# 아무거나 -> 차가운 아메리카노
def solution(order):
    answer = 0
    for i in order:
        if 'cafelatte' in i:
            answer += 5000
        elif 'americano' in i:
            answer += 4500
        elif i == 'anything':
            answer += 4500
            
    return answer
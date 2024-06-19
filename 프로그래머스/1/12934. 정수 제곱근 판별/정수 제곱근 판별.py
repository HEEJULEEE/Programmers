def solution(n):
    answer = -1
    if n % (n**0.5) == 0:
        answer = ((n**0.5)+1)**2
    return answer
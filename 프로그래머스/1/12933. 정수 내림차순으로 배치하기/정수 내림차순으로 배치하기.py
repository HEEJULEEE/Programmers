def solution(n):
    answer = ''
    s = [i for i in str(n)]
    s = sorted(s, reverse = True)
    answer = ''.join(i for i in s)
    return int(answer)
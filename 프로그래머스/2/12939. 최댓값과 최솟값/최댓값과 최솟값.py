def solution(s):
    int_list = [int(i) for i in s.split(" ")]
    return f"{min(int_list)} {max(int_list)}"
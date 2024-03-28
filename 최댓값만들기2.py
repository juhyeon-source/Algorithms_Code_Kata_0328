def solution(numbers):
    number_list = sorted(numbers)
    a = number_list[0] * number_list[1]
    b = number_list[-1] * number_list[-2]
    return max(a,b)
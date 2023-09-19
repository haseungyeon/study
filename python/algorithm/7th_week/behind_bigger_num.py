def recursive():
    return

def solution(numbers:list):
    answer = [-1 for _ in range(len(numbers))]
    max_num = numbers.pop()
    max_index = -1
    for index in reversed(range(len(numbers))):
        if max_num >= numbers[index]:
            answer[index] = numbers.pop(max_index)
            max_index = index
            break
        elif max_num < numbers[index]:
            # max_num = numbers.pop(max_index)
            max_index = index
        

        # if answer[index] == -1:
        #     max_num = cur_num

    return answer

numbers = [2, 3, 3, 5]
print(solution(numbers))

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))

numbers = [8, 9, 9, 8, 7, 5]


# def solution(numbers):
#     answer = [-1 for _ in range(len(numbers))]
#     for index in range(len(numbers)):
#         cur_num = numbers[index]
#         for next_num in numbers[index+1:]:
#             if next_num > cur_num:
#                 answer[index] = next_num
#                 break
#     return answer
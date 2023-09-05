# 리턴 조건 : 배열의 길이에 도달했을 경우
# 재귀함수 이용
# 마지막에 도달했을 경우 index 1 증가
import math

def solution(triangle:list):
    answer = 0
    
    total = [0 for _ in range(int(math.pow(2, len(triangle)-1)))]
    height = len(triangle)
    print(total)
    marking = [[False]*len(floor) for floor in triangle]

    print(marking)
    while True:
        sum_index = 0
        for triangle_index, floor in enumerate(triangle):
            for floor_index, floor_var in enumerate(floor):
                marking[triangle_index][floor_index] = True
                if triangle_index - floor_index <= 1:
                    sum_index += floor_index
                    total[sum_index] += floor_var
                # if triangle_index == height-1 and floor:
        print(total)
                
    # while False not in total:
        # index = 0
        # for triangle_index, floor in enumerate(triangle):
        #     if triangle_index != len(triangle)-1:
        #         total[index] += floor[index]
        #     answer += floor[index]
            # if floor[index] > floor[index+1]
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)
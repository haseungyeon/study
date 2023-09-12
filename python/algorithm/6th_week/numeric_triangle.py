# 리턴 조건 : 배열의 길이에 도달했을 경우
# 재귀함수 이용
# 마지막에 도달했을 경우 index 1 증가
import math

def solution(triangle:list):
    answer = 0
    
    total = [0 for _ in range(int(math.pow(2, len(triangle)-1)))]
    print(total)
    marking = [[False]*len(floor) for floor in triangle]

    print(marking)
    sum_index = 0
    sum_var = 0
    triangle_index = 0
    floor_index = 0
    finish_count = 0
    while finish_count < len(total)-1:
        # if floor_index <= triangle_index + 1:
        if triangle_index+1 < len(triangle) \
            and marking[triangle_index+1][floor_index] == False:
                
            triangle_index += 1
            
            marking[triangle_index][floor_index] = True
            sum_index += floor_index
            sum_var += triangle[triangle_index][floor_index]
        elif triangle_index+1 < len(triangle) \
            and floor_index+1 < len(triangle[triangle_index]) \
            and marking[triangle_index+1][floor_index] == True \
            and marking[triangle_index+1][floor_index+1] == False:
                
            triangle_index += 1 # 우, 하 한 칸 전진
            floor_index += 1
            
            marking[triangle_index][floor_index] = True # 마킹 후 전진한 위치의 주소 및 값 누적
            sum_index += floor_index
            sum_var += triangle[triangle_index][floor_index]
        elif triangle_index+1 < len(triangle) \
            and marking[triangle_index+1][floor_index] == True \
            and marking[triangle_index+1][floor_index+1] == True: # 아래, 아래 우측이 이미 계산되었을 경우 다시 한 층 위로
            triangle_index -= 1
            sum_index -= floor_index
            sum_var -= triangle[triangle_index][floor_index]
        elif triangle_index+1 == len(triangle):
            total[sum_index] = sum_var
            finish_count += 1
                
    print(total)
    print(marking)
        # triangle_index += 1
        # for triangle_index, floor in enumerate(triangle):
        #     for floor_index, floor_var in enumerate(floor):
        #         marking[triangle_index][floor_index] = True
        #         # if triangle_index - floor_index <= 1:
        #         sum_index += floor_index
        #         sum_var += floor_var
        #         if triangle_index+1 < len(triangle) and marking[triangle_index+1][floor_index] == False:
        #             break
        #         elif triangle_index+1 < len(triangle) and marking[triangle_index+1][floor_index] == True and marking[triangle_index][floor_index+1] == False:
        #             continue
        #         elif triangle_index+1 == len(triangle):
        #             total[sum_index] = sum_var
        #         else:
                    
                # if triangle_index == height-1 and floor:
                
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
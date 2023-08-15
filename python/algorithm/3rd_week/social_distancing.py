# 0이 될 조건
# 1칸 간격 P 연속등장
# 2칸 간격 대각일 경우 2방향 중 파티션이 하나라도 없는 경우, 직선일 경우 P 사이에 파티션이 없는 경우

def solution(places):
    answer = [1 for _ in range(len(places))]
    coordinate = {}
    for num, place in enumerate(places):
        coordinate.setdefault(num, {})
        for index_col, col in enumerate(place):
            for index_row, value in enumerate(col):
                coordinate[num].setdefault((index_col, index_row), value)
    for coordinate_num in coordinate:
        for col, row in coordinate[coordinate_num]:
            if coordinate[coordinate_num][col, row] == "P":
                # 1칸 차이날 경우 거리두기가 지켜지지 않는 조건
                if col+1 < 5 and coordinate[coordinate_num][col+1, row] == "P":
                    answer[coordinate_num] = 0
                    break
                if row+1 < 5 and coordinate[coordinate_num][col, row+1] == "P":
                    answer[coordinate_num] = 0
                    break

                # 2칸 차이날 경우 거리두기가 지켜지지 않는 조건
                if (col+1 < 5 and row-1 >= 0) and coordinate[coordinate_num][col+1, row-1] == "P":
                    if coordinate[coordinate_num][col+1, row] != "X" or coordinate[coordinate_num][col, row-1] != "X":
                        answer[coordinate_num] = 0
                        break
                if col+2 < 5 and coordinate[coordinate_num][col+2, row] == "P":
                    if coordinate[coordinate_num][col+1, row] != "X":
                        answer[coordinate_num] = 0
                        break
                if (col+1 < 5 and row+1 < 5) and coordinate[coordinate_num][col+1, row+1] == "P":
                    if coordinate[coordinate_num][col+1, row] != "X" or coordinate[coordinate_num][col, row+1] != "X":
                        answer[coordinate_num] = 0
                        break
                if row+2 < 5 and coordinate[coordinate_num][col, row+2] == "P":
                    if coordinate[coordinate_num][col, row+1] != "X":
                        answer[coordinate_num] = 0
                        break
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))

{0:{(0, 0): 'P', (0, 1): 'O'}}

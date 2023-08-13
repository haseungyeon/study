def solution(places):
    answer = []
    coordinate = {}
    for num, place in enumerate(places):
        coordinate.setdefault(num, {})
        for index_row, row in enumerate(place):
            for index_col, value in enumerate(row):
                coordinate[num].setdefault((index_row, index_col), value)
    for num in coordinate:
        for row, col in coordinate[num]:
            print(row, col)
            if coordinate[num][row, col] == "P":
                # coordinate.update({num: {(index_row, index_col): value}})
                # coordinate[num][index_row, index_col] = value
    print(coordinate)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)

{0:{(0, 0): 'P', (0, 1): 'O'}}
def solution(rows, columns, queries):
    answer = []
    rectangular = [[(i+1)+j*rows for i in range(columns)] for j in range(rows)]
    # print(rectangular)
    for query in queries:
        row_up    = query[0]-1
        col_left  = query[1]-1
        row_down  = query[2]-1
        col_right = query[3]-1
        rotate_right_list = tuple(rectangular[row_up][col_left:col_right])
        # print(rotate_right_list)
        rotate_down_list  = tuple(rectangular[top_down][col_right] for top_down in range(row_up, row_down))
        # print(rotate_down_list)
        rotate_left_list  = tuple(rectangular[row_down][col_right:col_left:-1])
        # print(rotate_left_list)
        rotate_up_list    = tuple(rectangular[down_top][col_left] for down_top in range(row_down, row_up, -1))
        # print(rotate_up_list)
        answer.append(min(min(rotate_right_list), min(rotate_down_list), min(rotate_left_list), min(rotate_up_list)))
        # 회전 방향으로 인덱스 1씩 증감
        for index, value in enumerate(rotate_right_list):
            rectangular[row_up][col_left+index+1] = value 
        for index, value in enumerate(rotate_down_list):
            rectangular[row_up+index+1][col_right] = value
        for index, value in enumerate(rotate_left_list):
            rectangular[row_down][col_right-index-1] = value
        for index, value in enumerate(rotate_up_list):
            rectangular[row_down-index-1][col_left] = value
        # print(rectangular)
    return answer

# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

# rows = 3
# columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

# rows = 100
# columns = 97
# queries = [[1,1,100,97]]

rows = 5
columns = 4
queries = [[1,1,5,4]]
print(solution(rows, columns, queries))
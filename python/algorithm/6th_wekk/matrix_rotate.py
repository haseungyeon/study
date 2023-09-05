def solution(rows, columns, queries):
    answer = []
    rectangular = [[(i+1)+j*6  for i in range(rows)] for j in range(columns)]
    print(rectangular)
    right_move_list = (queries[0]-1, queries[1]-1), (queries[0]-1, queries[3]-1)
    down_move_list  = queries[3], queries[3]
    left_move_list  = queries[2],
    up_move_list    = queries
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)
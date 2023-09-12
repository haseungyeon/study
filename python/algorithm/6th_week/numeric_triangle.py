def solution(triangle):
    sum_triangle = [[0]*len(floor) for floor in triangle]
    sum_triangle[0][0] = triangle[0][0]
    for ver in range(len(triangle)):
        for hor in range(ver):
            if hor == 0:
                sum_triangle[ver][hor] = sum_triangle[ver-1][hor]+triangle[ver][hor]
            else:
                sum_triangle[ver][hor] = max(sum_triangle[ver-1][hor-1], sum_triangle[ver-1][hor])+triangle[ver][hor]
            sum_triangle[ver][hor+1] = sum_triangle[ver-1][hor]+triangle[ver][hor+1]
    answer = max(sum_triangle[-1])

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)
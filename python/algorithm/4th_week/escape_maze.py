from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # 방향 설정 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 시작 지점, 출구, 레버 위치 찾기
    start = None
    end = None
    lever = None
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
    
    # BFS 탐색 시작
    queue = deque([(start[0], start[1], 0)])  # (행, 열, 현재까지 걸린 시간)
    visited = set([(start[0], start[1])])
    
    while queue:
        row, col, time = queue.popleft()
        
        if (row, col) == (end[0], end[1]):
            return time
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc # 사방으로 한 칸씩 진행
            
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if maps[new_row][new_col] != 'X':
                    queue.append((new_row, new_col, time + 1))
                    visited.add((new_row, new_col))
                    
                    # 레버를 만난 경우
                    if (new_row, new_col) == lever:
                        queue.append((new_row, new_col, time + 2))  # 레버를 당기는 시간 추가
    
    # 탈출할 수 없는 경우
    return -1
maps = [
    "SOOOOXXOOOOX",
    "XOXXOOXOOXXX",
    "OOOOOXOOOOOX",
    "OXXXXXOOXXXX",
    "OOOOOOOOOOOE"
]
solution(maps)
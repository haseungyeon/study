from collections import deque
def solution(N, M):
    is_eaten= deque()
    for _ in range(N):
        is_eaten.append(False)
    cnt = 0
    while True:
        cnt += 1
        is_eaten.popleft()
        is_eaten.appendleft(True)
        # print(list(is_eaten))
        try:
            is_eaten.rotate(M)
            if is_eaten.index(False, 0, 1):
                continue
        except:
            return cnt
solution(10, 4)
# print(solution(10, 4))
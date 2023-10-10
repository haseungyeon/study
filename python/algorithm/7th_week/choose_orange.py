from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    counts_of_orange = defaultdict(int)
    for orange in tangerine:
        counts_of_orange[orange] += 1 # 오렌지 크기를 키로, 수를 값으로 갖는 딕셔너리
    counts_of_orange = sorted(counts_of_orange.items(), key=lambda x:x[1]) # 오렌지 수로 정렬
    while k > 0: # 최소 종류를 위해선 가장 많은 오렌지 수부터 차례대로 k가 0이하가 될 때까지 순차적으로 담야야 할 갯수를 빼주며 종류의 수를 카운팅 해준다.
        k -= counts_of_orange.pop()[1]
        answer += 1
    return answer
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 6
print(solution(k, tangerine))
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 4
print(solution(k, tangerine))
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
k = 1
print(solution(k, tangerine))
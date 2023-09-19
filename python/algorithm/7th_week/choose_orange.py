from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    counts_of_orange = defaultdict(int)
    for orange in tangerine:
        counts_of_orange[orange] += 1
    counts_of_orange = sorted(counts_of_orange.items(), key=lambda x:x[1])
    while k > 0:
        k -= counts_of_orange.pop()[1]
        answer += 1
    print(counts_of_orange)
    
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
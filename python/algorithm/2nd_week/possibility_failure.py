from collections import defaultdict
def solution(N, stages:list):
    answer = []
    zero_failure = []
    stage_info = defaultdict(int)
    for stage in stages:
        stage_info[stage] += 1
    whole_stages = list(range(1, N+1))
    for stage in whole_stages:
        if stage not in stage_info.keys():
            zero_failure.append(stage)
    stage_info = sorted(stage_info.items())
    print(stage_info)
        # stage_info[stage] = list(stage_info[stage])
    for n in range(0, N):
        stage_info[n] = list(stage_info[n])
        stage_info[n].append(0)
        for m in range(n, N):
            stage_info[n][2] += stage_info[m][1]
    # answer = list(range())
    stage_info_dict = {}
    for v in stage_info:
        stage_info_dict[stage_info[v[0]]] = stage_info[v[1]]/stage_info[v[2]]
    stage_info_dict = dict(stage_info_dict.items())
    # stage_info.sort(stage_info[1]/stage_info[2])
    print(stage_info_dict)
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
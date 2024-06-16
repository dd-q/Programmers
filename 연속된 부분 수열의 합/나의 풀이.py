# ** 시간 초과 **


sequence = [1, 2, 3, 4, 5]
k = 7

def sol(sequence, k):
    answer = []

    size = len(sequence)

    indexTmp = [] # 조건에 만족하는 index 셋 찾기 위한 임시 변수
    indexes = [] # 조건에 만족하는 index 셋

    # 조건에 만족하는 index 셋 찾기
    for i in range(0, size):
        sumTmp = [] # 합계 임시 변수
        if len(indexTmp) == 0: # index 셋이 초기화 되었으면, 다시 index 부여 시작하도록.
            indexTmp.append(i)
        for j in range(i, size):
            sumTmp.append(sequence[j])
            if sum(sumTmp) > k:
                indexTmp = [] # 만족하는 인덱스 셋을 찾기 위한 임시 변수 초기화
                break # 숫자가 오름차순으로 정렬되어 있으므로 더 이상 진행하지 않아도 된다.
            if sum(sumTmp) == k:
                indexTmp.append(j) # 조건에 만족하는 index 셋 완성.
                indexes.append(indexTmp)
                indexTmp = [] # 초기화

    # 조건을 만족하는 하나의 값을 찾기 위한 변수
    mini = 100001
    for i in indexes: # 조건을 만족하는 인덱스 셋이 많다면, 최소값 + 가장 빠른 인덱스 값을 변별해야함
        if mini > i[1] - i[0]:
            mini = i[1] - i[0]
            answer = i

    return answer


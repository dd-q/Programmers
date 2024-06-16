
# 구글링한 다양한 해답들을 제출해도, 실패하는 경우가 동일하게 생김. 무슨 문제인지 모르겠음.

# sequence = [1, 2, 3, 4, 5]
sequence = [1, 1, 1, 2, 3, 4, 5]

# k = 7
k = 10

answer = []

# start, end = 0, 0
prefix_sum = sequence[0] # 부분 수열의 합
min_len = 10001 # 최소 길이


end = 0
sums = 0
for start in range(len(sequence)):
    while end < len(sequence) and sums < k:
        sums += sequence[end]
        end += 1
    if sums == k:
        if min_len > end - start:
            answer = [start, end - 1]
        min_len = min(min_len, end-start)
    sums -= sequence[start]



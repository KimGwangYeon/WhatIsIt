def solution(numbers):
    answer = []
    for i, val in enumerate(numbers):   # 인덱스와 벨류값을 한번에 뽑아쓴 유용한 함수이다.
        re_range = numbers[i + 1:]

        for j in re_range:
            answer.append(val + j)

    return sorted(set(answer))
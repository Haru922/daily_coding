def solution(A):
    total=sum(A)
    min_value=max(A)-min(A)
    part=0
    for i in range(len(A)-1):
        part+=A[i]
        min_value=min(min_value,abs(total-part*2))
    return min_value

def solution(A, K):
    K=K%len(A) if len(A) else 0
    return A[len(A)-K:]+A[:len(A)-K]

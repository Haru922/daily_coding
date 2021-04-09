def solution(A, B, K):
    return B//K-A//K if A%K else B//K-A//K+1

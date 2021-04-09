def solution(X, A):
    position=-1
    leaves=set()
    for i in range(len(A)):
        leaves.add(i)
        if len(leaves)==X:
            position=i
            break
    return position

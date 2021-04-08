def solution(A):
    i=0
    A.sort()
    while i<len(A)-1:
        if A[i]!=A[i+1]:
            if i==0 and A[i+1]!=A[i+2]:
                i+=1
            break
        i+=2
    return A[i]

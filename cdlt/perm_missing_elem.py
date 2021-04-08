def solution(A):
    answer=1
    if len(A):
        A.sort()
        if A[0]!=1:
            answer=1
        elif A[-1]!=len(A)+1:
            answer=len(A)+1
        else:
            for i in range(len(A)-1):
                if A[i]+1!=A[i+1]:
                    answer=A[i]+1
                    break
    return answer

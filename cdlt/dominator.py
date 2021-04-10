def solution(A):
    num_count={}
    dominator=-1
    for i in range(len(A)):
        if A[i] not in num_count:
            num_count[A[i]]=0
        num_count[A[i]]+=1
        if num_count[A[i]]>len(A)//2:
            dominator=i
            break
    return dominator

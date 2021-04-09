def solution(A):
    missing=1
    A.sort()
    for num in A:
        if num>0:
            if num==missing:
                missing+=1
            elif num>missing:
                break
    return missing

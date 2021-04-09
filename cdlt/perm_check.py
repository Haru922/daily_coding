def solution(A):
    return_value=order=1
    A.sort()
    for num in A:
        if num!=order:
            return_value=0
            break
        order+=1
    return return_value

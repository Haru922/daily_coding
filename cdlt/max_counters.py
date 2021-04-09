def solution(N, A):
    counter=[0]*N
    max_counter=last_max_value=0
    for num in A:
        if num<=N:
            counters[num-1]+=1
            max_counter=max(max_counter,counters[num-1])
        else:
            if last_max_value<max_counter:
                last_max_value=max_counter
                counters=[max_counter]*N
    return max_counter

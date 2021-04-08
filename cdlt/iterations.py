def solution(N):
    binary_n=[]
    while (N):
        binary_n.append(N%2)
        N//=2
    max_gap=gap_cnt=0
    in_gap=False
    for n in binary_n:
        if n==1:
            if in_gap:
                max_gap=max(max_gap,gap_cnt)
                gap_cnt=0
            else:
                in_gap=True
        else:
            if in_gap:
                gap_cnt+=1
    return max_gap

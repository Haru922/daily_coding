def solution(S, P, Q):
    answer=[]
    length=len(S)
    dna_a=[0]*length
    dna_c=[0]*length
    dna_g=[0]*length
    if S[0]=='A':
        dna_a[0]=1
    elif S[0]=='C':
        dna_c[0]=1
    elif S[0]=='G':
        dna_g[0]=1
    for i in range(1,length):
        dna_a[i]=dna_a[i-1]
        dna_c[i]=dna_c[i-1]
        dna_g[i]=dna_g[i-1]
        if S[i]=='A':
            dna_a[i]+=1
        elif S[i]=='C':
            dna_c[i]+=1
        elif S[i]=='G':
            dna_g[i]+=1
    for p,q in zip(P,Q):
        nucleotide=4
        if p:
            if dna_a[q]-dna_a[p-1]:
                nucleotide=1
            elif dna_c[q]-dna_c[p-1]:
                nucleotide=2
            elif dna_g[q]-dna_g[p-1]:
                nucleotide=3
        else:
            if dna_a[q]:
                nucleotide=1
            elif dna_c[q]:
                nucleotide=2
            elif dna_g[q]:
                nucleotide=3
        answer.append(nucleotide)
    return answer

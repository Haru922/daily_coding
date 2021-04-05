def jumpingOnClouds(c,k):
    pos=k%len(c)
    energy=99-2*c[pos]
    while pos:
        pos=(pos+k)%len(c)
        energy-=(1+2*c[pos])
    return energy

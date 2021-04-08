def solution(X, Y, D):
    return round((Y-X)/D+0.5) if (Y-X)%D else (Y-X)//D

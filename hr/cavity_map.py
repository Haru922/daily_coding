def cavityMap(grid):
    n=len(grid)
    r_str=[]
    if n>1:
        r_str.append(grid[0])
    for i in range(1,n-1):
        line=[]
        for j in range(n):
            cur=grid[i][j]
            if 0<j and j<n-1:
                max_num=max(int(grid[i-1][j]),int(grid[i+1][j]),int(grid[i][j-1]),int(grid[i][j+1]))
                cur='X' if max_num<int(grid[i][j]) else grid[i][j]
            line.append(cur)
        r_str.append(''.join(line))
    r_str.append(grid[n-1])
    return r_str

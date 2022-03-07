def parse_matrix(r):
    m = [[int(s) for s in input().split(" ")] for i in range(r)]
    return m


def compute_possibilities(r, c):
    l = []
    for j in range(2,r+1):
        if 2*j <= c:
            l.append((j, 2*j))
        else:
            break
    
    for j in range(4, r+1, 2):
        if j/2 <= c:
            l.append((j, int(j/2)))
    
    return l

def search_row(number, matrix):
    pass

def search_column(number, matrix, rc, cc, r):
    a = 0
    if rc+number <= r:
        if sum( [matrix[k][cc] for k in range(rc,rc+number) ] ) == number:
            a+=1
    if rc-number >=-1:
        if sum( [matrix[k][cc] for k in range(rc,rc-number,-1) ]) == number:
            a+=1
    return a
    
t = int(input())
for k in range(1,t+1):
    r,c = (int(s) for s in input().split(" "))
    pos = compute_possibilities(r, c)
    m = parse_matrix(r)
    count = 0

    top = [[0 for i in range(c)] for j in range(r)]
    left = [[0 for i in range(c)] for j in range(r)]

    bottom =[[0 for i in range(c)] for j in range(r)]
    #bottom[r-1] = [0 if m[r-1][j]==0 else 1 for j in range(c)]

    right = [[0 for i in range(c)] for j in range(r)]
    #for i in range(r):
     #   right[i][-1] = 0 if m[i][-1]==0 else 1

    for i in range(r):
        for j in range(c):
            if m[i][j] == 0:
                continue
            top[i][j] = top[i-1][j] + 1
            left[i][j] = left[i][j-1] +1
    
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            if m[i][j] == 0:
                continue
            bottom[i][j] = bottom[(i+1)%r][j] + 1
            right[i][j] = right[i][(j+1)%c] +1

    for i in range(r):
        for j in range(c):
            if (top[i][j], left[i][j]):
                count += max(min(top[i][j]//2,left[i][j]) + min(left[i][j]//2,top[i][j]) -2, 0)
            if (top[i][j], right[i][j]):
                count += max(min(top[i][j]//2,right[i][j]) + min(right[i][j]//2,top[i][j]) -2, 0)
            if (bottom[i][j], right[i][j]):
                count +=max(min(bottom[i][j]//2,right[i][j]) + min(right[i][j]//2,bottom[i][j]) -2, 0)
            if (bottom[i][j], left[i][j]):
                count += max(min(bottom[i][j]//2,left[i][j]) + min(left[i][j]//2,bottom[i][j]) -2, 0)
    print(f'Case #{k}: {count}')


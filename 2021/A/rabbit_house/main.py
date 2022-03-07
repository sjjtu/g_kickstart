import heapq

def parse_matrix(r):
    m = [[-int(s) for s in input().split(" ")] for i in range(r)]
    return m

def get_next_max(m, r, c, already_visited):
    _i, _j = (0, 0)
    _m = 0
    for i in range(r):
        for j in range(c):
            if m[i][j] >= _m and (i,j) not in already_visited:
                _i, _j = i, j
                _m = m[i][j]
    return _i, _j 

def correct_cross(i, j, m, r, c):
    count = 0
    center = m[i][j]
    #print(m[i][j])
    if i+1 < r:
        count += max(abs(m[i+1][j]-m[i][j])-1,0)
        if max(abs(m[i+1][j]-m[i][j])-1,0)>0:
            m[i+1][j] = center+1
            entry_finder[(i+1,j)][-1] = ""
            del entry_finder[(i+1,j)]
            entry = [m[i+1][j], (i+1,j), "a"]
            heapq.heappush(hq, entry)
            entry_finder[entry[-2]] =entry

            #print(f"changing {i+1}{j}")
    
    if i-1 > -1:
        count += max(abs(m[i-1][j]-m[i][j])-1,0)
        if max(abs(m[i-1][j]-m[i][j])-1,0)>0:
            m[i-1][j] = 1+center
            entry_finder[(i-1,j)][-1] = ""
            del entry_finder[(i-1,j)]
            entry = [m[i-1][j], (i-1,j), "a"]
            heapq.heappush(hq, entry)
            entry_finder[entry[-2]] =entry
            #print(f"changing {i-1}{j}")
    if j+1 < c:
        count += max(abs(m[i][j+1]-m[i][j])-1,0)
        if max(abs(m[i][j+1]-m[i][j])-1,0)>0:
            m[i][j+1] = 1+center
            entry_finder[(i,j+1)][-1] = ""
            del entry_finder[(i,j+1)]
            entry = [m[i][j+1], (i,j+1), "a"]
            heapq.heappush(hq, entry)
            entry_finder[entry[-2]] =entry
            #print(f"changing {i}{j+1}")
    if j-1 > -1:
        count += max(abs(m[i][j-1]-m[i][j])-1,0)
        if max(abs(m[i][j-1]-m[i][j])-1,0)>0:
            m[i][j-1] = 1+center
            entry_finder[(i,j-1)][-1] = ""
            del entry_finder[(i,j-1)]
            entry = [m[i][j-1], (i,j-1), "a"]
            heapq.heappush(hq, entry)
            entry_finder[entry[-2]] =entry
            #print(f"changing {i}{j-1}")
    #print(count)
    #print(hq)
    return count

t = int(input())
for k in range(1,t+1):
    r,c = (int(s) for s in input().split(" "))
    m = parse_matrix(r)
    count = 0
    hq = []
    entry_finder = {}

    for i in range(r):
        for j in range(c):
            entry = [m[i][j], (i,j), "a"]
            heapq.heappush(hq, entry)
            entry_finder[entry[-2]] = entry

    #print(entry_finder)

    while hq:
        #print(entry_finder)
        entry = heapq.heappop(hq)
        if entry[-1]:
            del entry_finder[entry[-2]]

            count += correct_cross(*entry[1], m, r, c)
            #print(entry)
            
               
    print(f'Case #{k}: {count}')


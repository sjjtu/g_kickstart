import heapq
from heapq import *
import itertools

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

def parse_matrix(r, v=False):
    if v:
        m = [int(s) for s in input().split(" ")]
    else:
        m = [[int(s) for s in input().split(" ")] for i in range(r)]
    return m

def deduce(i,j):
    #print(f'working on {i,j}')
    #print(f'unknowns: {r_u[i], c_u[j]}')
    if r_u[i]==1 or c_u[j]==1:
        r_u[i] = max(r_u[i]-1, 0)
        c_u[j] = max(c_u[j]-1, 0)
        return 0 
    elif r_u[i]==0 or c_u[j]==0:
        return 0 
    else:
        r_u[i] = max(r_u[i]-1, 0)
        c_u[j] = max(c_u[j]-1, 0)
        return B[i][j]

def unkown():
    ru = []
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += 0 if B[i][j]==0 else 1
        ru.append(temp)

    cu = []
    for j in range(n):
        temp = 0
        for i in range(n):
            temp += 0 if B[i][j]==0 else 1
        cu.append(temp)
    return ru, cu

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

t = int(input())
for k in range(1,t+1):
    n = int(input())
    A = parse_matrix(n)
    B = parse_matrix(n)
    for i in range(n):
        for j in range(n):
            add_task((i,j), B[i][j])
    R = parse_matrix(1, v=True)
    C = parse_matrix(1, v=True)

    r_u, c_u = unkown()

    count = 0

    while pq:
        i, j = pop_task()
        #print(i,j)
        #print(r_u)
        #print(c_u)
        
        count += deduce(i,j)
               
    print(f'Case #{k}: {count}')


#DFS Uninformed search
graph={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':[],'F':[]}

def dfs(n,visited=[]):
    if n not in visited:
        visited.append(n)
        for x in graph[n]: dfs(x,visited)
    return visited

print("DFS:",dfs('A'))


#Greedy Search Informed search 
import heapq
graph={'A':['B','C'],'B':['D'],'C':['D'],'D':[]}
h={'A':3,'B':2,'C':1,'D':0}
q=[(h['A'],'A')]
while q:
    _,n=heapq.heappop(q); print(n,end=" ")
    if n=='D': break
    for x in graph[n]: heapq.heappush(q,(h[x],x))

#Hill climbing 
values = [1, 3, 5, 4, 2]
current = 0

while current+1 < len(values) and values[current+1] > values[current]:
    current += 1

print("Best value:", values[current]) 


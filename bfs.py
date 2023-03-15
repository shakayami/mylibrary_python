from collections import deque
N,M=map(int,input().split())
G=[[] for i in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    #1-indexedの場合は
    #a-=1;b-=1
    G[a].append(b)
    #無向グラフの場合は
    #G[b].append(a)
#初期地点
st=0
q=deque([st])
dist=[-1 for i in range(N)]
dist[st]=0
prev=[-1 for i in range(N)]
while(q):
    r=q.popleft()
    for p in G[r]:
        if dist[p]==-1:
            dist[p]=dist[r]+1
            prev[p]=r
            q.append(p)
print(*dist)
print(*prev)

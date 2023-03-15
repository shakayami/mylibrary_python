from heapq import heappush,heappop
N,M=map(int,input().split())
G=[[] for i in range(N)]
for _ in range(M):
    a,b,c=map(int,input().split())
    #1-indexedの場合は
    #a-=1;b-=1
    G[a].append((b,c))
    #無向グラフの場合は
    #G[b].append((a,c))

INF=10**18
dist=[INF for i in range(N)]
st=0
dist[st]=0
q=[]
heappush(q,(0,st))
while(q):
    nowdis,v=heappop(q)
    if dist[v]<nowdis:
        continue
    for u,w in G[v]:
        if dist[u]>dist[v]+w:
            dist[u]=dist[v]+w
            heappush(q,(dist[u],u))
print(*dist)

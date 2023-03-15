#再帰は使ってないけど
#あまり早くはないかも
# https://atcoder.jp/contests/abc291/tasks/abc291_h
from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
G=[[] for i in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    a-=1;b-=1
    G[a].append(b)
    G[b].append(a)
ans=[-1 for i in range(N)]
prev=[-1 for i in range(N)]
dist=[-1 for i in range(N)]
size=[0 for i in range(N)]
is_determine=[False for i in range(N)]
deq=deque([0])
dist[0]=0
while(deq):
    nroot=deq.popleft()
    q=deque([nroot])
    children=[nroot]
    while(q):
        r=q.popleft()
        for p in G[r]:
            if dist[p]==-1:
                dist[p]=dist[r]+1
                prev[p]=r
                children.append(p)
                q.append(p)
    vertex=sorted(children,key=lambda x:-dist[x])
    for v in vertex:
        size[v]=1
        for u in G[v]:
            if u==prev[v]:
                continue
            if is_determine[u]:
                continue
            size[v]+=size[u]
    center=nroot
    ndepth=dist[nroot]
    while(True):
        child=[x for x in G[center] if x!=prev[center] and not(is_determine[x])]
        if not child:
            break
        j=max([(size[i],i) for i in child])[1]
        if size[j]*2<=size[nroot]:
            break
        else:
            center=j
    is_determine[center]=True
    prev[nroot],prev[center]=prev[center],prev[nroot]
    dist[nroot],dist[center]=dist[center],dist[nroot]
    size[nroot],size[center]=size[center],size[nroot]
    
    for x in children:
        if x!=center:
            dist[x]=-1
            prev[x]=-1
            size[x]=0
    for p in G[center]:
        if is_determine[p]:
            pass
        else:
            deq.append(p)
            prev[p]=center
            dist[p]=dist[center]+1
for i in range(N):
    if prev[i]!=-1:
        prev[i]+=1
print(*prev)

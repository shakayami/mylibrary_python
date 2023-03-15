# https://atcoder.jp/contests/past202005-open/tasks/past202005_m

from collections import deque
N,M=map(int,input().split())
G=[[] for i in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    u-=1;v-=1
    G[u].append(v)
    G[v].append(u)
s=int(input())-1
K=int(input())
t=[int(i)-1 for i in input().split()]+[s]
def bfs(st):
    q=deque([st])
    res=[-1 for i in range(N)]
    res[st]=0
    while(q):
        r=q.popleft()
        for p in G[r]:
            if res[p]!=-1:
                continue
            res[p]=res[r]+1
            q.append(p)
    return res

dist=[[0 for j in range(K+1)]for i in range(K+1)]
for i in range(K+1):
    dis=bfs(t[i])
    for j in range(K+1):
        dist[i][j]=dis[t[j]]
INF=10**18
dp=[[INF for j in range(K+1)] for i in range(1<<K)]
dp[0][K]=0
for S in range(1<<K):
    for i in range(K):
        if (S&(1<<i))==0:
            for j in range(K+1):
                dp[S|(1<<i)][i]=min(dp[S|(1<<i)][i],dp[S][j]+dist[j][i])
print(min(dp[-1]))

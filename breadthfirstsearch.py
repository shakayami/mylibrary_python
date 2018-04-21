import queue
def rectlist(x,A,B):
    return [[x for i in range(M)] for i in range(N)]
INF = 10**8
N,M=map(int,input().split())
maze=[list(input()) for i in range(N)]
d=rectlist(INF,N,M)
s=(0,0)
g=(0,0)
for i in range(N):
    for j in range(M):
        if maze[i][j]=="S":
            s=(i,j)
        elif maze[i][j]=="G":
            g=(i,j)
dR=[(1,0),(-1,0),(0,1),(0,-1)]
d[s[0]][s[1]]=0
q=queue.Queue()
q.put(s)
while(not(q.empty())):
    r=q.get()
    x=r[0];y=r[1]
    if (x==g[0] and y==g[1]):
        break
    for dr in dR:
        nx=x+dr[0]
        ny=y+dr[1]
        if 0<=nx<N and 0<=ny<M:
            if maze[nx][ny]!="#" and d[nx][ny]==INF:
                q.put((nx,ny))
                d[nx][ny]=d[r[0]][r[1]]+1
print(d[g[0]][g[1]])

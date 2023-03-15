N,M=map(int,input().split())
F=[list(input()) for i in range(N)]
def dfs(x,y):
    F[x][y]="."
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<M:
                if F[nx][ny]=="W":
                    dfs(nx,ny)
ans=0
for i in range(N):
    for j in range(M):
        if F[i][j]=="W":
            dfs(i,j)
            ans+=1
print(ans)

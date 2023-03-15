#https://atcoder.jp/contests/abc293/tasks/abc293_g

from collections import defaultdict
import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
A=[int(i) for i in input().split()]
query=[]
for i in range(Q):
    l,r=map(int,input().split())
    l,r=min(l,r),max(l,r)
    query.append((l-1,r,i))
def int_sqrt(n):
    low=0
    high=n+10
    while(high-low>1):
        mid=(high+low)//2
        if mid*mid<=n:
            low=mid
        else:
            high=mid
    return low
Qsqrt=int_sqrt(Q)
B=1+N//Qsqrt
query.sort(key=lambda x:(x[0]//B,x[1]*(-1+2*((x[0]//B)%2)),x[2]))
l=0
r=0
nowans=0
#ランダムアクセスの遅いdefaultdictを使うと定数倍で死ぬ可能性があるので注意
nowdict=[0 for i in range(202020)]
ans=[0 for i in range(Q)]
for j in range(Q):
    nl,nr,nidx=query[j]
    if l<nl:
        while(l<nl):
            b=nowdict[A[l]]
            nowdict[A[l]]-=1
            nowans-=((b*(b-1)*(b-2))//6)
            nowans+=(((b-3)*(b-1)*(b-2))//6)
            l+=1
    elif l>nl:
        while(l>nl):
            b=nowdict[A[l-1]]
            nowdict[A[l-1]]+=1
            nowans-=((b*(b-1)*(b-2))//6)
            nowans+=((b*(b-1)*(b+1))//6)
            l-=1
    else:
        pass
    if r<nr:
        while(r<nr):
            b=nowdict[A[r]]
            nowdict[A[r]]+=1
            nowans-=((b*(b-1)*(b-2)))//6
            nowans+=((b*(b-1)*(b+1)))//6
            r+=1
    elif r>nr:
        while(r>nr):
            b=nowdict[A[r-1]]
            nowdict[A[r-1]]-=1
            nowans-=((b*(b-1)*(b-2))//6)
            nowans+=(((b-3)*(b-1)*(b-2))//6)
            r-=1
    else:
        pass
    ans[nidx]=nowans
print(*ans,sep="\n")

#https://atcoder.jp/contests/abc198/tasks/abc198_f
mod=998244353
#場合によってはpolynomial_prodの部分をFFT convolutionで計算することもある。
def polynomial_prod(P1,P2):
    n1=len(P1)
    n2=len(P2)
    res=[0 for i in range(n1+n2-1)]
    for i1 in range(n1):
        for i2 in range(n2):
            res[i1+i2]+=P1[i1]*P2[i2]
            res[i1+i2]%=mod
    return res
def bostan_mori_algorithm(P,Q,N):
    #[x^N] P(x)/Q(x)
    while(N>0):
        Qd=[(x*(-1)**(i%2))%mod for i,x in enumerate(Q)]
        V=polynomial_prod(Q,Qd)
        U=polynomial_prod(P,Qd)
        Q=V[::2]
        P=U[N%2::2]
        N//=2
    return P[0]*pow(Q[0],mod-2,mod)%mod
N=int(input())
P=[0,0,0,0,0,0,1,0,0,0,1,1,3]
Q=[1,-1,-2,0,2,4,-1,-3,-3,-1,4,2,0,-2,-1,1]
ans=bostan_mori_algorithm(P,Q,N)
print(ans)


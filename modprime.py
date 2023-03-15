mod=998244353
#もしくは
#mod=10**9+7
def inv(x):
    assert x!=0
    return pow(x,mod-2,mod)

MAX_N=10**5
Fact=[0 for i in range(MAX_N+1)]
Fact[0]=1
for i in range(MAX_N):
    Fact[i+1]=((i+1)*Fact[i])%mod
Finv=[0 for i in range(MAX_N+1)]
Finv[MAX_N]=inv(Fact[MAX_N])
for i in range(MAX_N-1,-1,-1):
    Finv[i]=((i+1)*Finv[i+1])%mod

def binomial(n,k):
    if 0<=k and k<=n:
        return Fact[n]*Finv[k]%mod*Finv[n-k]%mod
    else:
        return 0

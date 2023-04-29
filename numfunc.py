from math import gcd
from collections import Counter

#最大公約数
def lcm(x,y):
    return (x*y)//gcd(x,y)

#素因数分解
def prime_fact(N):
    res=Counter()
    p=2
    while(p*p<=N):
        while(N%p==0):
            N//=p
            res[p]+=1
        p+=1
    if N>1:
        res[N]+=1
    return res

#約数列挙
def divisors(N):
    PF=prime_fact(N)
    res=[1]
    for p,e in PF.items():
        k=len(res)
        for i in range(k*e):
            res.append(res[i]*p)
    return res

#エラトステネスのふるい
MAX_N=10**5
isPrime=[True for i in range(MAX_N+1)]
isPrime[0]=False;isPrime[1]=False
for i in range(MAX_N+1):
    if isPrime[i]:
        for j in range(2*i,MAX_N+1,i):
            isPrime[j]=False
print(isPrime[:10])
#[False, False, True, True, False, True, False, True, False, False]
#メビウス関数
Mebius=[1 for i in range(MAX_N+1)]
Mebius[0]=0
for i in range(MAX_N+1):
    if isPrime[i]:
        for j in range(i,MAX_N+1,i):
            Mebius[j]*=-1
i=2
while(i*i<=MAX_N):
    for j in range(i*i,MAX_N+1,i*i):
        Mebius[j]=0
    i+=1
print(Mebius[:20])
#[0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0, -1, 0, -1]

def powFp2(r,n):
    if n==0:return Fp2(1,0)
    elif n%2==1:return r*powFp2(r,n-1)
    else:return powFp2(r*r,n//2)
class Fp2():
    a=0
    b=0
    def __init__(self,A,B):
        self.a=A%mod
        self.b=B%mod
    def __add__(self,other):
        return Fp2((self.a+other.a)%mod,(self.b+other.b)%mod)
    def __sub__(self,other):
        return Fp2((self.a-other.a)%mod,(self.b-other.b)%mod)
    def __mul__(self,other):
        return Fp2((self.a*other.a+5*self.b*other.b)%mod,(self.b*other.a+self.a*other.b)%mod)
    def __truediv__(self,other):
        othernum=inv(other.a**2-5*other.b**2)
        otherinv=Fp2((other.a*othernum)%mod,(-other.b*othernum)%mod)
        return self*otherinv
    def __iadd__(self,other):
        self.a+=other.a
        self.b+=other.b
        self.a%=mod
        self.b%=mod
        return self
    def __isub__(self,other):
        self.a-=other.a
        self.b-=other.b
        self.a%=mod
        self.b%=mod
        return self
    def __str__(self):
        return f'Fp2({self.a},{self.b})'
 

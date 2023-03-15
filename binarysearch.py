# https://atcoder.jp/contests/arc050/submissions/20570855
# https://atcoder.jp/contests/arc050/tasks/arc050_b
R,B=map(int,input().split())
x,y=map(int,input().split())
def check(K):
    if R-K<0 or B-K<0:
        return False
    tmp=(R-K)//(x-1)+(B-K)//(y-1)
    if tmp>=K:
        return True
    else:
        return False
#check(K)という関数は、「花束をK個以上作ることが可能か？」という関数である。
#ここで、checkという関数は単調性がある。
#つまり、check(x)=True,check(y)=Falseならばx<yが成り立つ。
#ここでlow,highを設定する
#このとき初期状態は必ずcheck(low)=True,check(high)=Falseであるようにする
low=0
high=10**300
while(high-low>1):
    #ループの中において、low,highの値は変わるが、
    #check(low)=True,check(high)=Falseという状態は常に保存されている。
    #保存されている状態のまま、high-lowがループ一回ごとに約1/2になる
    mid=(high+low)//2
    if check(mid):
        low=mid
    else:
        high=mid
#最終的にループを脱出したとき、high-low=1となってる。
#このときlowはcheck(low)=Trueをみたす最大の数となり、
#一方highはcheck(high)=Falseをみたす最小の数となる。
print(low)

low=0
#答えの上限が不明な場合、以下のようにすることもできる。
high=1
while(check(high)):
    high*=2

#ループを脱出した時点で、check(high)=Falseが成立している
#あとは同じ
while(high-low>1):
    mid=(high+low)//2
    if check(mid):
        low=mid
    else:
        high=mid
print(low)

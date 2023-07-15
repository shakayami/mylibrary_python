'''
部分和として10を含むパターンは少ない

'''
from functools import lru_cache
@lru_cache(maxsize=10**6)
def partition(n,k):
    #k個の1以上の変数で総和がn
    if n==0:
        if k==0:
            return [[]]
        else:
            return []
    elif n<k:
        return []
    elif k==0:
        return []
    else:
        return [[1]+[x for x in seq]for seq in partition(n-1,k-1)]+[[x+1 for x in seq]for seq in partition(n-k,k)]
def partition_list(n):
    res=[]
    for k in range(n+1):
        res+=partition(n,k)
    return res
for seq in partition_list(10):
    print(*seq)
'''
実行例
10
1 9
2 8
3 7
4 6
5 5
1 1 8
1 2 7
1 3 6
1 4 5
2 2 6
2 3 5
2 4 4
3 3 4
1 1 1 7
1 1 2 6
1 1 3 5
1 1 4 4
1 2 2 5
1 2 3 4
1 3 3 3
2 2 2 4
2 2 3 3
1 1 1 1 6
1 1 1 2 5
1 1 1 3 4
1 1 2 2 4
1 1 2 3 3
1 2 2 2 3
2 2 2 2 2
1 1 1 1 1 5
1 1 1 1 2 4
1 1 1 1 3 3
1 1 1 2 2 3
1 1 2 2 2 2
1 1 1 1 1 1 4
1 1 1 1 1 2 3
1 1 1 1 2 2 2
1 1 1 1 1 1 1 3
1 1 1 1 1 1 2 2
1 1 1 1 1 1 1 1 2
1 1 1 1 1 1 1 1 1 1
'''

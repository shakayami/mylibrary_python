A,B=3,2
#切り捨て（床関数）
F=A//B
#切り上げ（天井関数）
C=-(-A//B)
#もしくは
C=(A+B-1)//B
print(F,C)

'''
mathのRound関数は厳密には四捨五入してくれない
（小数部分が0.5である場合は偶数の方に丸め込まれる）

浮動小数点演算は誤差を含むので競プロにおいては//演算子を使うのが良いのかも

'''

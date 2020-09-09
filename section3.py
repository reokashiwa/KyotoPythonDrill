# 3.2.2 代入順序のお話。
a = 1 + 2
a = 3 + 4
print(a)

# 変数名として使えるのは、
# * 英大文字
# * 英小文字 (大文字と小文字は区別される。)
# * 数字
# * アンダースコア
# 変数名の規則は
# * 数字を先頭に使ってはいけない。
# * 予約語は使えない。
# 変数名は冒頭は小文字でなければならないといった規則はない。
# ただし大文字で始まる変数は定数としてつかわれがちなので好まれない。
# 
# PEP8
# https://www.python.org/dev/peps/pep-0008/

# 3.4 代入演算子
a = 1
print(a)
# => 1
a = a + 1
print(a)
# => 2

kakaku = 1000
nebikiritsu = 15
kakaku = kakaku * (100 - nebikiritsu) / 100
# 誤植
print(kakaku)
# => 850.0
print(kakaku.__class__)
# => <class 'float'>

# 代入演算子いろいろ
# += (ex. a += b === a = a + b)
# -= (ex. a -= b === a = a - b)
# *= (ex. a *= b === a = a * b)
# /= (ex. a /= b === a = a / b)

# ++ や -- はありません。

print(2**100)
# => 1267650600228229401496703205376
# 誤植?

# Pythonのデータ型
# int()
# float()
# str()
# bool()
# なぜ()をつけるんだろうね。そのうちわかるだろう。

a = 1
b = 1 / 2
c = "ABC"
print(a)
# => 1
print(b)
# => 0.5
print(c)
# => ABC
print(type(a))
# => <class 'int'>
print(type(b))
# => <class 'float'>
print(type(c))
# => <class 'str'>

# ここでtype()の説明が入るんだけど、それはおまえsection2で出て来たやろと。


# 3.8.1 sqrtの実装
x = 2
rnew = x
r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
print(r1, rnew, r2)
# => 2 1.5 1.0
r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
print(r1, rnew, r2)
# => 1.5 1.4166666666666665 1.3333333333333333

r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
print(r1, rnew, r2)
# => 1.4166666666666665 1.4142156862745097 1.411764705882353

r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
print(r1, rnew, r2)
# => 1.4142156862745097 1.4142135623746899 1.41421143847487

r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
print(r1, rnew, r2)
# => 1.4142135623746899 1.414213562373095 1.4142135623715002
# 強引 :-)
# しかしこのアルゴリズム(ニュートン法)、よくわからない。ちょっと考えよう。

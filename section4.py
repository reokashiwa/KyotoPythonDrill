# 4.2
# exercise 13.
# 3.8.1 を制御構造を用いて再実装する。
x = 2
rnew = x

# range()もbuild-in functionです。
# class range(stop)
# class range(start, stop[, step])
# Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.
for i in range(10):
    r1 = rnew
    r2 = x / r1
    rnew = (r1 + r2) / 2
    print(r1, rnew, r2)

# exercise 14.
x = 2
rnew = x
for i in range(10):
    r1 = rnew
    r2 = x / r1
    rnew = (r1 + r2) / 2
print(r1, rnew, r2)

# exercise 14.
x = 2
rnew = x
for pow in range(8):
    loop = 10 ** pow
    for i in range(loop):
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
    print(r1, rnew, r2)

# program 5
for i in range(10):
    if i == 1:# i == 1 のときはprint(i)に至らず、次の値に進みます。
        continue
    if i == 8:# i == 8 のときもprint(i)に至らず、ループから抜けます。
        break 
    print(i)
# => 8

# 4.6
print(list(range(10)))
# exercise 17
print(list(range(10,20)))
print(list(range(10,100,10)))

# program 6
for i in range(3):
    for j in range(3):
        print(i,j)

# exercise 17
for i in range(3):
    for j in range(i):
        print(i,j)

# program 7
for i in ["三条", "四条", "五条" ]:
    for j in ["河原町" , "烏丸" , "堀川" ]:
        cross = i+j
        print(cross)

# program 8
# x の平方根を求める
x = 2
rnew = x
diff = rnew - x/rnew
if (diff < 0):
    diff = -diff

while (diff > 1.0E-6):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if (diff < 0):
        diff = - diff

# program 9 (improvement of program 8)
x = 2
rnew = x

while True:
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if (diff < 0):
        diff = - diff
    if diff <= 1.0E-6:
        break

# 4.10.1
print('a' in 'abc')

# 4.10.3
# 算術演算は比較演算よりも優先
# 比較演算は論理演算よりも優先
## おぼえてられっか!

# exercise 20
x = float(input("sqrt: "))
rnew = x

while True:
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if (diff < 0):
        diff = - diff
    if diff <= 1.0E-6:
        break

# program 12
while True:
    x = input("input positive number: " )
    try:
        x = float(x)
    except ValueError:
        print(x, " cannot cast to float." )
        continue
    except:
        print("Unexpected error." )
        exit()
    if (x <=0):
        print(x, "is not a positive number." )
        continue
    # 以下は正しい入力が得られた時の処理
    print(x)

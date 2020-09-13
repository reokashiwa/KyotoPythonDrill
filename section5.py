def square_root(x):
    'return square root value of x'
    rnew = x
    diff = abs(rnew - x/rnew)

    while (diff > 1.0E-6):
        r1 = rnew
        r2 = x/r1
        rnew = (r1 + r2)/2
        print(r1, rnew, r2)
        diff = abs(r1 - r2)

    return rnew

# v = 2
# print("Root square of ", v, " is ", square_root(v))

def get_positive_numeral():
    while True:
        num = input("Input a number you want to sqrt: " )

        try:
            x = float(num)
        except ValueError:
            print(num, " cannot cast to float.")
            continue
        except:
            print("Unexpected error.")
            exit()

        return x

while True:
    x = get_positive_numeral()
    if (x >=0):
        print("Root square of ", x, " is ", square_root(x))
    else:
        print(x, " is a negative number.")

# uses farey sequence algorithm to find a rational approximation of a number
# x = numerator. y = denominator
# 2025 note: doesn't work for some reason?

def main():
    n = float(input("Enter a decimal: "))
    xl = 0
    xu = yl = yu = 1
    for i in range(10000):
        x = xl + xu
        y = yl + yu
        f = x/y
        if n < f:
            xu = x
            yu = y
        elif n > f:
            xl = x
            yl = y
        elif n == f:
            print("{}/{}".format(x,y))
            return
    print("{}/{}".format(x,y))

main()

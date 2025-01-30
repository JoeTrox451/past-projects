# File: primefinder.py
# checks whether a number is prime, returns the smallest prime factor if not

from math import sqrt

def main():
    x = int(input("Enter a number: "))
    for i in range(2,int(sqrt(x))+1):
        y = x%i
        if y == 0:
            print(x, "is divsible by", str(i) + ".")
            return
    print(x, "is prime.")
    return


main()
    

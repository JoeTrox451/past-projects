# File: fibonacci.py
# Prints a number of fiponacci numbers

def main():
    print ("This program prints a specified amount of fibonacci numbers")
    print()
    quan = int(input("Enter the amount of numbers to print: "))
    x = 0
    y = 1
    print(1)
    for i in range(quan//2):
        x = x + y
        print(x)
        y=y+x
        print(y)
        

main()

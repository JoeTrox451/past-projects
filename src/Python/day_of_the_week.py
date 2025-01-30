# File: dotw.py
# determines the day of the week a particular date is
# does not work for dates before 1753
# 2025 note: This program uses a algorithm found in the book __

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def start():
    print("\nThis program determines the day of the week a particular date is")
    print("Note: The date must be after 1752 because of the English")
    main()

def main():
    try:
        month, day, year = input("Enter the date using the format mm/dd/yyyy: ").split("/")
        m = int(month)
        d = int(day)
        y = int(year)
        if m < 0 or m > 12 or d < 0 or d > 31 or y <= 1752:
            raise ValueError
        elif m == 2 and y%4 != 0 and d > 28:
            raise ValueError
        elif m == 2 and y%4 == 0 and d > 29:
            raise ValueError
        elif m == 4 and d > 30:
            raise ValueError
        elif m == 6 and d > 30:
            raise ValueError
        elif m == 9 and d > 30:
            raise ValueError
        elif m == 11 and d > 30:
            raise ValueError
    except ValueError:
        print("\nYou did not enter a valid date, or the year was not after 1752")
        main()
    k = int(0.6 + (1/m))
    l = y - k
    o = m + 12*k
    p = l/100
    z1 = int(p/4)
    z2 = int(p)
    z3 = int((5*l)/4)
    z4 = int(13*(o+1)/5)
    z5 = z4 + z3 - z2 + z1 + d - 1
    z = z5 - (7*int(z5/7))
    print("\nThe day of the week is", days[z])
    runAgain()


def runAgain():
    c = input("\nDo you want to try another date? ") + " "
    if c[0].lower() == "y":
        main()
    else:
        print("Have a good day!")
        input("Press <Enter> to quit.\n")
        quit()


start()

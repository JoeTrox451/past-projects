def main(op):
    time1 = input("Enter a time in hh:mm:ss\n")
    time2 = input("Enter a time in hh:mm:ss\n")
    try:
        h1,m1,s1 = time1.split(":")
        h1 = int(h1)
        m1 = int(m1)
        s1 = int(s1)
        h2,m2,s2 = time2.split(":")
        h2 = int(h2)
        m2 = int(m2)
        s2 = int(s2)
    except:
        print("Wrong, try again")
        quit()
    seconds1 = (h1*3600) + (m1*60) + s1
    seconds2 = (h2*3600) + (m2*60) + s2
    if seconds1 > seconds2:
        seconds1, seconds2 = seconds2, seconds1
    if op == "add":
        final = seconds1 + seconds2
    else:
        final = seconds2 - seconds1
    print(final, "seconds")
    hours = final//3600
    minutes = (final-hours*3600)//60
    seconds = (final-hours*3600-minutes*60)%60
    print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))


main("sub")

# Recursively lists the factorial of an number
def main(num):
    if num <= 0:
        return 1
    else:
        return main(num-1) * num



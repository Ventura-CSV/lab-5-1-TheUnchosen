def getinput():
    # ******************************
    # Make your Code
    # ******************************
    num = int(input("type in an input "))
    return num



def getsum(v1, v2):
    # ******************************
    # Make your Code
    # ******************************
    num = v1 + v2
    return num


def printval(v1, v2, total):
    # ******************************
    # Make your Code
    # ******************************
    print(v1, v2, total)


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()

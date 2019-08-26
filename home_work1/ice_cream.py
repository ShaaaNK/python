def ice_cream():
    print("Ice cream balls ")
    ice_cream_balls = int(input())

    if ice_cream_balls % 3 == 0 or ice_cream_balls % 5 == 0 or ice_cream_balls > 7:
        print("YES")
    else:
        print("False")


if __name__ == '__main__':
    ice_cream()

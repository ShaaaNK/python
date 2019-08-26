def entrance():
    print("Flat's numbers")

    a = int(input())
    b = int(input())

    c = b - a + 1

    if b % c == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    entrance()

def variable_swap():

    print("A:")
    a = int(input())

    print("B:")
    b = int(input())

    a = a + b
    b = a - b
    a = a - b

    print("Second number a= ", a)
    print("first number b = ", b)


if __name__ == '__main__':
    variable_swap()

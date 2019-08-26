def simple_calc():

    print("Введите номер операции, которую хотите выполнить\n "
          "1. Сложение \n 2. Вычитание \n 3. Умножение \n 4. Деление\n ")
    choose_sign = int(input())

    print("Введите число b")
    operator_one = int(input())
    print("Введите число c")
    operator_two = int(input())

    if choose_sign == 1:
        print(operator_two + operator_one)

    elif choose_sign == 2:
        print(operator_one - operator_two)

    elif choose_sign == 3:
        print(operator_one * operator_two)

    elif choose_sign == 4:
        private = operator_one // operator_two
        remainder = operator_one % operator_two
        print("Частное ", private, "Остаток", remainder)

    else:
        print("Введите число от 1 до 4")


if __name__ == '__main__':
    simple_calc()

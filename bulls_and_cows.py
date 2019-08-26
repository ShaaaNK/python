def guess_number():
    user_number = []
    count = 0
    secret_number = input('Введите секретное число \n')
    if len(secret_number) != 4:
        print("Введённое вами число должно состоять из 4 цифр! "
              "Перезапустите программу")
    else:
        while user_number != secret_number:
            user_number = input("Введите ваше число \n")
            if len(user_number) != len(secret_number):
                print("Введённое вами число должно состоять из 4 цифр")
                count += 1
                continue
            count += 1
            print("Попытка ", count, "\n")
            cows = count_cows(secret_number, user_number)
            bulls = count_bulls(secret_number, user_number)
            print("Коров ", cows, "Быков ", bulls)
        print("Вы победили! Затратив всего ", count, " попыток")


def count_bulls(secret_number, user_number):
    count_bulls = 0
    for i in range(0, 4):
        if user_number[i] == secret_number[i]:
            count_bulls += 1
    return count_bulls


def count_cows(secret_number, user_number):
    count_cows = 0
    for i in range(0, 4):
        if user_number[i] in secret_number:
            count_cows += 1
    return count_cows


if __name__ == '__main__':
    guess_number()

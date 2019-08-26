def king_move():
    chess_figure = int(input("Для того чтобы сделать ход введите номер фигуры: "
                             "\n 1. Король \n 2. Ферзь \n 3. Ладья \n"))
    old_x = int(input("Ввердите координату X:"))
    old_y = int(input("Ввердите координату Y:"))
    new_x = int(input("Ввердите новую координату X:"))
    new_y = int(input("Ввердите новую координату Y:"))

    if 8 < new_x >= 0 or 8 < new_y >= 0 or 8 < old_x >= 0 or 8 < old_y >= 0:
        print("Координаты должны быть больше 0 и меньше 8! ")

    if old_x == new_x and old_y == new_y:
        print("Вы остались на том же месте! сделайте ход")

    if chess_figure == 1:
        if (abs(new_x - old_x) == 1 or old_x == new_x) \
                and (abs(new_y - old_y) == 1 or old_y == new_y):
            print("YES")
        else:
            print("NO")

    elif chess_figure == 2:
        if abs(old_x - new_x) == abs(old_y - new_y) or old_x == new_x or old_y == new_y:
            print("YES")
        else:
            print("No")

    elif chess_figure == 3:
        if old_x == new_x or old_y == new_y:
            print("YES")
        else:
            print("No")


if __name__ == '__main__':
    king_move()

import os
import shop


def show_menu():
    """
    Показывает главное меню
    TODO:
    И него начинается игра или заканчивается программа
        Настройка цвет: текста
        Сохранение/загрузка
    """

    # главний цикл меню б завершается правильным выбором
    while True:
        os.system("cls")
        print("1 - Начить новую игру")
        print("2 - выйти")
        answer = input("Введте номер ответа и нажмите ENTER")
        if answer == "1":
            start_game()
            break
        elif answer == "2":
            print("Выходим из игры")
            break
    print("Выходим из меню! Пока!")


def start_game():
    """
    Создают персонажа:
        player_name - имя игрока
        player_maney - деньги игрока
        player_hp - жизни игрока, >= 0
        player_xp - опыт игрока
        player_pt - зелья игрока при использования лечит
    Запускаем игру
    Игра конролируется переменной is_game
    """

    # Создаем игрока КОРТЕЖ
    player_name = input("Введите имя игрока и нажите ENTER")
    player_hp = 100
    player_maney = 50
    player_xp = 0
    player_pt = 0
    player = (player_name, player_maney, player_hp, player_xp, player_pt)


    is_game = True
    while is_game:
        os.system("cls")
        print(f"имя:", player[0])
        print(f"деньги", player[1])
        print(f"жизни", player[2])
        print(f"опыт", player[3])
        print(f"зелья", player[4])
        print("1 - Поеду-ка я где убитому быть. Умру в чистом поле, как славный богатырь")
        print("2 - Ну, поеду где богатому быть")
        print("3 - Ну, поеду в магазин")


        answer = input("Введите номер ответа и нажмите ENTER ")


        if answer == "1":
            print("Поехал на битву")
        if answer == "2":
            print("Поехал в казино")
        if answer == "3":
            player = shop.shop(player)

        input("Нажмите ENTER для продолжения")




show_menu()
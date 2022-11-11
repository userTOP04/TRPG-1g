import os
import shop
from random import randint, choice


first_names = ("Жран", "Дрын", "Брысь", "Морти")
last_names =  ("Борзый", "Вонючий" , "Злой", "ЛОХ")

def make_hero(
        name=None,
        money=None,
        hp=None,
        xp=None,
        at=None,
        df=None,
        pt=None
) -> tuple:
    if not name:
        name = f"{choice(first_names)} {choice(last_names)}"
    if not money:
        money = randint(1, 50)
    if not hp:
        hp = randint(1, 100)
    if not xp:
        xp = randint(0, 5)
    if not at:
        at = randint(1, 5)
    if not df:
        df = randint(1, 10)
    if not pt:
        pt = randint(0, 3)
    return (name, money, hp, xp, at, df, pt)

player = make_hero(name="Безымянный", money=50, hp=100, xp=0, at=1, df=0, pt=0)

prototupe = make_hero()
prototupe1 = make_hero()
prototupe2 = make_hero()


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
    player = make_hero(pt=5)


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
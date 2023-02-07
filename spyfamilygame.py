from random import randint, choice
import os


def make_hero(
        name=None,
        hp_now=None,
        hp_max=None,
        lvl=1,
        xp_now=0,
        attack=1,
        defence=1,
        weapon=None,
        shield=None,
        luck=1,
        money=None,
        inventory=None,
) -> dict:

    if not hp_now:
        hp_now = randint(1, 100)
    
    if not hp_max:
        hp_max = hp_now

    xp_next = lvl * 100

    if money is None:
        money = randint(0, 100)

    if not inventory:
        inventory = []

    if not weapon:
        weapon = {
            "тип": "оружие",
            "название": "Обычный меч",
            "стат": "атака",
            "модификатор": 2,
            "цена": 10
        }
    
    return {
        "имя": name,
        "здоровье": hp_now,
        "здоровье макс": hp_max,
        "уровень": lvl,
        "опыт": xp_now,
        "опыт след": xp_next,
        "оружие": weapon,
        "щит": shield,
        "атака": attack,
        "защита": defence,
        "удача": luck,
        "деньги": money,
        "инвентарь": inventory
    }






def show_hero(hero: dict) -> None:
    print("имя:", hero['имя'])
    print("здоровье:", hero['здоровье'], "/", hero['здоровье макс'])
    print("уровень:", hero['уровень'])
    print("опыт:", hero['опыт'], "/", hero['опыт след'])
    print("атака:", hero['атака'])
    print("защита:", hero['защита'])
    print("удача:", hero['удача'])
    print("деньги:", hero['деньги'])
    print("инвентарь:", hero['инвентарь'])



def show_options(hero: dict, options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def choose_option(hero: dict, options: list) -> int:
    """
    Получает ввод пользователя
    Проверяет ввод и возвращает его, если он есть в вариантах
    """
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except ValueError:
        print("Ввод должен быть целым неотрицательным числом")
        return choose_option(hero, options)
    else:
        if option < len(options) and option > -1:
            return option
        else:
            print("Нет такого выбора")
            return choose_option(hero, options)



def play_anua():
    Anua = make_hero(name="Аня Форджер",hp_max=50,hp_now=50,lvl=1,attack=1,money=0)
    print("Вы выбрали персонажа не сможите его поменять до конца игры, ваш персонаж Аня Форджер")
    show_hero(Anua)


def play_loud():
    Loud = make_hero(name="Лойд Форджер",hp_max=150,hp_now=150,lvl=30,attack=25,money=10000,inventory=["Пистолет"])
    print("Вы выбрали персонажа не сможите его поменять до конца игры, ваш персонаж Лойд Форджер")
    show_hero(Loud)

def play_your():
    Your = make_hero(name="Йор Форджер",hp_max=100,hp_now=100,lvl=20,attack=100,money=1000,inventory=["Ножи шипы"])
    print("Вы выбрали персонажа не сможите его поменять до конца игры, ваш персонаж Йор Форджер")
    show_hero(Your)


def play_game(hero: dict):
    print("приветствуем вас в игре пожалуйста выберите персонажа")
    options = [
        "Аня Форджер, способности: экстрасенс может читать мысли, слабости: маленькая девочка 6 лет, кодовое имя: нет",
        "Лойд Форджер, способность: мастер маскировки, шпион хорошо владеет огнестрельным оружием, слабости: нет, кодовое имя: сумрак",
        "Йор Форджер, способность: наемный убийца, хорошо владеет боевыми искуствами и своим оружием, слабости: нет, кодовое имя: принцеса шипов "
    ]
    show_options(hero, options)
    option = choose_option(hero, options)
    if option == 0:
        play_anua()    
    elif option == 1:
        play_loud()
    elif option == 2:
        play_your()
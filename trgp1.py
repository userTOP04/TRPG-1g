import os
from random import randint, choice



first_names = ("Жран", "Дрын", "Брысь", "Морти")
last_names =  ("Борзый", "Вонючий" , "Злой", "ЛОХ")



def make_hero(
    name=None,
    hp_now=None,
    lvl=1,
    xp_next=1000,
    xp_now=0,
    at=10,
    df=0,
    weapon=None,
    shielt=None,
    money=None,
    luck=1,
    inventory=None
) -> list:
    """
    Герой - это список
    [0] name - имя персонажа
    [1] hp_max - максимальное число жизней
    [2] hp_now - тукущее число жизней
    [3] lvl - максимальное число опыта
    [4] xp_next - опыта для следующего уровня
    [5] xp_now - текущий опыт
    [6] at - сила атаки
    [7] df - защита
    [8] weapon - оружие
    [9] shielt - щит
    [10] money - деньги
    [11] luck - удача
    [12] inventory - инвентарь
    """
    if not name:
        name = f"{choice(first_names)} {choice(last_names)}"
    if not hp_now:
        hp_now = randint(1, 100)
        hp_max = hp_now
    if money is None:
        money = randint(0, 50)
    if not inventory:
        inventory = []
    return [
        name,
        hp_max,
        hp_now,
        lvl,
        xp_next,
        xp_now,
        at,
        df,
        weapon,
        shielt,
        money,
        luck,
        inventory,
    ]



def print_hero(hero: list) -> None:
    print("имя:", hero[0],)
    print("жизни:", hero[2], "/", hero[1],)
    print("уровень:", hero[3],)
    print("опыт:", hero[5], "/", hero[4],)
    print("атака:", hero[6],)
    print("защита:", hero[7],)
    print("оружие:", hero[8],)
    print("щит:", hero[9],)
    print("деньги:", hero[10],)
    print("удача:", hero[11],)
    print("инвентарь:", hero[12])



def levelup(hero: list) -> None:
    if hero[5] >= hero[4]:
        hero[3] += 1
        hero[4] = hero[3] * 1000
        print("Уровень повышен, молодец")



pl = make_hero()
pl[5] += 1000
if pl[5] >= pl[4]:
    pl[3] += 1
    pl[4] = pl[3] * 1000
print_hero(pl)


pl1 = make_hero()
pl1[5] += 800
if pl1[5] >= pl1[4]:
    pl1[3] += 1
    pl1[4] = pl1[3] * 1000
print_hero(pl1)


def buy_item(hero: list, price: int) -> None:
    """

    [0] name - имя персонажа
    [10] money - деньги персонажа
    [12] inventory - инвентарь
    """

    if hero[10] >= price:
        hero[10] -= price
        hero[12].appent("зелье")
        print(f"{hero[0]} купил зелье за {price} монет!/n")
    else:
        print(f"{hero[0]} не хватило {price - hero[10]} монет!/n")


def consume_item(hero: list, idx):
    """

    Герой - это список
    [0] name - имя персонажа
    [1] hp_max - максимальное число жизней
    [2] hp_now - тукущее число жизней
    [3] lvl - максимальное число опыта
    [4] xp_next - опыта для следующего уровня
    [5] xp_now - текущий опыт
    [6] at - сила атаки
    [7] df - защита
    [8] weapon - оружие
    [9] shielt - щит
    [10] money - деньги
    [11] luck - удача
    [12] inventory - инвентарь
    """
    if idx =< len(hero[12]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[12][idx]}")


        if hero[12][idx] == "зелье":
            """

            [1] hp_max
            [2] hp_now
            """
            hp_now = xp_max
        elif hero[12][idx] == "яблоко"
            pass
        else:
            print("Употребил что то неизвестное")
    else:
        print("Нет такого предмета")






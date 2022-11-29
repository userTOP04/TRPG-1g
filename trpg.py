
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
    while hero[5] >= hero[4]:
        hero[3] += 1
        hero[4] = hero[3] * 1000
        print("Уровень повышен, молодец")




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


def consume_item(hero: list, item: str, idx):
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
    if idx <= len(hero[12]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[12][idx]}")


        if hero[12][idx] == "зелье":
            """
            [1] hp_max
            [2] hp_now
            """
            hero[2] += 10
            if hero[2] > hero[1]:
                hero[2] = hero[1]
        elif hero[12][idx] == "яблоко":
            print(f"{name} съел яблоко")
        else:
            print(f"{name} съел {hero[12][idx]}")
        hero[12].pop[ind]



def play_dice(hero: list, bet: int):
    if bet > 0:
        if bet <= hero[10]:
            hero_score = randint(2, 12)
            casino_store = randint(2, 12)
            print(f"{hero[0]} выбросил {hero_score}")
            print(f" трактирщик выбросил {casino_score}")
            if hero_score > casino_store:
                hero[10] += bet
                print(f"{hero[0]} победил и забирает {bet} монет")
            elif hero_score < casino_store:
                hero[10] -= bet
                print(f"{hero[0]} проиграл {bet} монет")
            else:
                print("Ничья")
        else:
            print(f"У {hero[0]} нет столько монет!")


def start_fight(hero: list):


    enemy = make_hero(name="ЛОХ",inventory=["Жопа Бобра", "ПАЛКА ЛОХА"], xp_now=1000)
    while hero[2] > 0 and enemy[2] > 0:
        combut_turn(hero, enemy)
        input(print(f"жизни {hero[2]} у {hero[0]} "))
        combut_turn(enemy, hero)
        input(print(f"жизни {enemy[2]} у {enemy[0]}"))
    os.system("cls")
    print("бой закончен")
    


def comdat_result(hero, enemy):
    """
    Если игрок победил:
        Забирает опыт, деньги, предметы игрока

    """
    os.system("cls")
    if hero[2] > 0 and enemy[2] <= 0:
        print(f"{hero[0]} победил противника {enemy[0]} ")
        print(enemy[5], "опыта")
        hero[10] += enemy[10]
        print(enemy[10], "монет")
        print("И забирает предметы")
        print(*enemy[12])
        hero[12] += enemy[12]
        levelup(hero)



def combut_turn(attacker: list, defender: list):
    if attacker[2] > 0:
        damage = attacker[6]
        defender[2] -= damage
        print(f"{attacker[0]} ударил {defender[0]} на {damage} здоровье")



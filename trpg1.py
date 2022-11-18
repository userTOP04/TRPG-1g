from random import randint, choice



first_names = ("Жран", "Дрын", "Брысь", "Морти")
last_names =  ("Борзый", "Вонючий" , "Злой", "ЛОХ")



def make_hero(
    name=None,
    hp_now=None,
    lvl=1,
    xp_next=None,
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
    xp_next = lvl * 1000
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





    print("имя:", hero[0])
    print("жизни:", hero[2] "/" hero[1])
    print("опыт:", )
    print("атака:", hero[6])
    print("защита:", hero[7])
    print(оружие)
    print(щит)
    print(деньги)
    print(удача)
    print(инвентарь)


levelup(hero: list)

pl = make_hero()
pl1 = make_hero()
print(pl)
print(pl1)
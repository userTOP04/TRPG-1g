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
        hero[12].append("зелье")
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


        if hero[12][idx] == "зелье лечение":
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
    if bet <= hero[10]:
        if bet > 0:
            if bet <= hero[10]:
                hero_score = randint(2, 12)
                casino_store = randint(2, 12)
                print(f"{hero[0]} выбросил {hero_score}")
                print(f" трактирщик выбросил {casino_store}")
                if hero_score > casino_store:
                    hero[10] += bet
                    print(f"{hero[0]} победил и забирает {bet} монет")
                elif hero_score < casino_store:
                    hero[10] -= bet
                    print(f"{hero[0]} проиграл {bet} монет")
                else:
                    print("Ничья")
                input("нажмите ENTER для продолжения")
            else:
                print(f"У {hero[0]} нет столько монет!")
                input("нажмите ENTER для продолжения")
    else:
        print("Вы не можете поставить столько монет потому что у вас их столько нет")
        input("нажмите ENTER для продолжения")


def start_fight(hero: list):


    enemy = make_hero(name="Злой питон", inventory=["мечь питона", "шит питона"], xp_now=2000, )
    while hero[2] > 0 and enemy[2] > 0:
        os.system("cls")
        combut_turn(hero, enemy)
        combut_turn(enemy, hero)
        print_hero(hero)
        print_hero(enemy)
        pause = input("Чтобы продолжить нажмите ENTER")
    os.system("cls")
    print("бой закончен")
    comdat_result(hero, enemy)
    


def comdat_result(hero, enemy):
    """
    Если игрок победил:
        Забирает опыт, деньги, предметы игрока
    """
    if hero[2] > 0 and enemy[2] <= 0:
        print(f"{hero[0]} победил противника {enemy[0]} ")
        hero[5] += enemy[5]
        print(enemy[5], "опыта")
        hero[10] += enemy[10]
        print(enemy[10], "монет")
        print("И забирает предметы")
        for item in enemy[12]:
            print(item, end=",")
        print(*enemy[12])
        hero[12] += enemy[12]
        levelup(hero)
    elif enemy[2] > 0 and hero[2] <=0:
        print(f"{enemy[0]} победил противника {hero[0]}")
        print("Игра окончена")
    else:
        print("Никто не победил. Ничья")
            


def combut_turn(attacker: list, defender: list):
    if attacker[2] > 0:
        damage = attacker[6]
        defender[2] -= damage
        print(f"{attacker[0]} ударил {defender[0]} на {damage} здоровье")


def choose_option(hero: list, text: str, options: list):
    print_hero(hero)
    print(text)
    for num, option in enumerate(options):
        print(f"{num}. {option}")
    option = input("\nВведите номер вариантаи нажмите ENTER: ")
    try:
        option = int(option)
    except: #Выполняем если трай не выполнился
        print("Ввод должен быть цулым неотрицательным числом")
    else:
        print("")
        if option < len(options) and option > -1:
            return option
        else:
            print("Нет такой опции")
    input("Пауза после выбора опции")


def visit_hub(hero: list):
    text = f"{hero[0]} приехал в хаб, сдесь есть чем заняться:"
    options = [
        "Заглянуть в лавку алхимика",
        "Заглянуть в трактир",
        "Поехать на арену",
        "Поехать обратно в главное меню"
    ]
    option = choose_option(hero, text, options)
    os.system("cls")
    if option == 0:
        return visit_shop(hero)
    elif option == 1:
        return visit_cosino(hero) 
    elif option == 2:
        return visit_arena(hero)   
    elif option == 3:
        print("Типо ушли в меню")  
    input("\n нажмите ENTER чтобы продолжить от хаба")



def visit_shop(hero: list):
    os.system("cls")
    text = f"{hero[0]} приехал в лавку алхимика, сдесь странно пахнут и продаются зелья:"
    options = [
    "Купить зелье лечение за 10 монет",
    "Приехать в хаб"
    ]
    input("В магазине")
    option = choose_option(hero, text, options)
    if option == 0:
        buy_item(hero, 10 )
        return visit_shop(hero)
    elif option == 1:
        visit_hub(hero)


def visit_cosino(hero: list):
    os.system("cls")
    input("в казино")
    text = f"{hero[0]} приехал в трактир, трактирщик предлогает сыграть на деньги "
    options = [
        "Сыграть на деньги с трактирщиком в кости",
        "Приехать в хаб"
    ]
    option = choose_option(hero, text, options)
    if option == 0:
        bet = int(input("Сделайте ставку"))
        play_dice(hero, bet)
        return visit_cosino(hero)    
    elif option == 1:
        visit_hub(hero)


def visit_arena(hero: list):
    os.system("cls")
    input("в казино")
    text = f"{hero[0]} приехал на арену где сражаются бойцы"
    options = [
        "Сражаться с бйцами",
        "Съесть предмет из инвенторя",
        "Уехать в хаб"
    ]
    if "зелье лечение" in hero[12]:
        options.append("Выпить зелье лечения")
    option = choose_option(hero, text, options)
    if option == 0:
        start_fight(hero)
    elif option == 1:
        idx = choose_option(hero, "", hero[12]) 
        os.system("cls")
        if idx is not None:
            consume_item(hero)  
    elif option == 2:
        visit_hub(hero)
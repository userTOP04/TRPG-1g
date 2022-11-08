
import os



def shop(player):

    name = player[0]
    hp = player[2]
    money = player[1]
    xp = player[3]
    pt = player[4]


    while True:

        os.system("cls")
        print(f"имя", name)
        print(f"жизьни", hp)
        print(f"деньги", money)
        print(f"опыт", xp)
        print(f"зелья", pt)

        print(f"{name} приехал в лавку")


        print("1 - Купить зелье за 10 монет")
        print("2 - Уехать к камню")


        answer = input("Введте номер ответа и нажмите ENTER")


        if answer == "1":
            os.system("cls")
            if money >= 10:
                money -= 10
                pt += 1
            else:
                print("недостадочно средств пшол вон")
            input("нажмите ENTER")

        elif answer == "2":
            return (name, hp, money, xp, pt)
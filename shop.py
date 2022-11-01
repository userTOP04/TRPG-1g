import os



def shop(player_name, player_maney, player_hp, player_xp, player_pt):
    while True:
        os.system("cls")
        print(f"имя: {player_name}")
        print(f"деньги: {player_maney}")
        print(f"жизни: {player_hp}")
        print(f"опыт: {player_xp}")
        print(f"зелья: {player_pt}")


        print(f"{player_name} приехал в лавку")


        print("1 - Купить зелье за 10 монет")
        print("2 - Уехать к камню")

        answer = input("Введте номер ответа и нажмите ENTER")
        if answer == "1":
            os.system("cls")
            if player_maney >= 10:
                player_maney -= 10
                player_pt += 1
            else:
                print("недостадочно средств пшол вон")
            input("Введте номер ответа и нажмите ENTER")






        elif answer == "2":
            break

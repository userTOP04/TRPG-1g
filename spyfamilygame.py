import os

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



play_game()
	text = "Приведствуем вас в игре spy family, выберите персонажа"
	options = [
		"Аня Форджер, способности: экстрасенс может читать мысли, слабости: маленькая девочка 6 лет",
		"Лойд Форджер, способность: мастер маскировки, шпион хорошо владеет огнестрельным оружием, слабости: нет",
		""
	]
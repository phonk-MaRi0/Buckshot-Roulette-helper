import os

print("\nПеред началом введи количество патронов\n"
      "Например: '5 1' (5 холостых, 1 боевой)\n"
      "х - холостой, б - боевой, гг - рестарт.\n")

def clear_console():
    """Очищает консоль."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_ammo_input():
    """Получает от пользователя количество холостых и боевых патронов."""
    while True:
        input_str = input("количество холостых и боевых: ")
        parts = input_str.split()

        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            print("заново введи")
            continue

        holost, boevie = map(int, parts)

        if holost < 0 or boevie < 0:
            print("заново введи")
            continue

        total_rounds = holost + boevie
        if total_rounds == 0:
            print("заново введи")
            continue

        print('шанс боевого:', round((boevie / total_rounds) * 100), '%')

        return holost, boevie


def buckshot_roulette():
    """Игра в русскую рулетку с дробовиком."""
    while True:  # Цикл для повторных игр
        holost, boevie = get_ammo_input()
        rounds = holost + boevie
        total_rounds = 0

        clear_console()
        print("холостых:", holost,
              "боевых:", boevie,
              "всего:", rounds)


        while rounds > 0:
            type_shot = input('').lower()

            if type_shot == 'гг':
                clear_console()
                print("\nrestart.....\n\n\n\n")
                break  # Выход из внутреннего цикла, чтобы начать новую игру

            if type_shot == 'х' and holost > 0:
                holost -= 1
                total_rounds += 1
                shot_type = "холостой ----"
            elif type_shot == 'б' and boevie > 0:
                boevie -= 1
                total_rounds += 1
                shot_type = "боевой   ----"
            else:
                print('заново введи')
                continue  # Возврат к началу цикла

            rounds = holost + boevie #update rounds value

            print("выстрел:", total_rounds,
                  shot_type,
                  "холостых:", holost,
                  "боевых:", boevie,
                  "осталось:", rounds)

            if rounds > 0:
                print('шанс боевого:', round((boevie / rounds) * 100), '%')
            else:
                print("\nrestart.....\n\n\n\n")


if __name__ == "__main__":
    buckshot_roulette()

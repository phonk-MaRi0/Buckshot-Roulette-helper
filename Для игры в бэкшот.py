import time
import os


def clear_console():
    """Очищает консоль."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_ammo_input():
    """Получает от пользователя количество холостых и боевых патронов."""
    while True:
        input_str = input("Введите количество холостых и боевых патронов (через пробел): ")
        parts = input_str.split()

        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            print("Ошибка: Введите два целых числа через пробел.")
            continue

        holost, boevie = map(int, parts)

        if holost < 0 or boevie < 0:
            print("Ошибка: Количество патронов не может быть отрицательным.")
            continue

        total_rounds = holost + boevie
        if total_rounds == 0:
            print("Ошибка: Общее количество патронов не может быть равно нулю.")
            continue


        print('Шанс боевого:', round((boevie / total_rounds) * 100), '%')

        return holost, boevie


def buckshot_roulette():
    """Игра в русскую рулетку с дробовиком."""
    while True:  # Цикл для повторных игр
        holost, boevie = get_ammo_input()
        rounds = holost + boevie
        total_rounds = 0
        clear_console()
        print(f"Холостых: {holost}, Боевых: {boevie}, Всего: {rounds}")

        while rounds > 0:
            type_shot = input("Выберите тип выстрела ('х' - холостой, 'б' - боевой, 'r' - перезапуск): ").lower()

            if type_shot == 'r':
                clear_console()
                print("\nПерезапуск игры...\n")
                break  # Выход из внутреннего цикла, чтобы начать новую игру

            if type_shot == 'х' and holost > 0:
                holost -= 1
                total_rounds += 1
                shot_type = "холостой"
            elif type_shot == 'б' and boevie > 0:
                boevie -= 1
                total_rounds += 1
                shot_type = "боевой"
            else:
                print("Некорректный ввод или недостаточно патронов данного типа.")
                continue  # Возврат к началу цикла

            rounds = holost + boevie #update rounds value

            print(f"Выстрел: {total_rounds}, {shot_type} ---- Холостых: {holost}, Боевых: {boevie}, Осталось: {rounds}")

            if rounds > 0:
                print('Шанс боевого:', round((boevie / rounds) * 100), '%')
            else:
                print("game over")

        if rounds == 0:
            print("\nrestart....\n")
            break  # Выход из внешнего цикла (завершение программы)


if __name__ == "__main__":
    buckshot_roulette()

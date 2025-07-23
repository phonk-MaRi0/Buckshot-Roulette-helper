import time


def get_ammo_input():
    while True:
        input_str = input("количество холостых и боевых: ")
        parts = input_str.split()

        if len(parts) != 2 or not (parts[0].isdigit() and parts[1].isdigit()):
            print("заново введи")
            continue

        holost, boevie = map(int, parts)

        if holost < 0 or boevie < 0:
            print("заново введи")
            continue

        print('шанс боевого:', round((boevie/(holost + boevie))*100),'%')
        
        return holost, boevie


def buckshot_roulette():
    holost, boevie = get_ammo_input()
    print("холостых:", holost,
          "боевых:", boevie,
          "всего:", holost + boevie)

    rounds = holost + boevie
    total_rounds = 0
    while rounds > 0:
        type_shot = input('').lower()

        if type_shot in ('гг', 'uu', 'пп', 'gg'):
            time.sleep(0.5)
            print('\nrestart.....\n\n\n\n\n')
            time.sleep(0.5)
            buckshot_roulette()

        if type_shot in ('х', '[') and holost > 0:
            holost -= 1
            total_rounds += 1
            print("выстрел:", total_rounds,
                  "холостой ----",
                  "холостых:", holost,
                  "боевых:", boevie,
                  "осталось:", holost + boevie)

        elif type_shot in ('б', ',') and boevie > 0:
            boevie -= 1
            total_rounds += 1
            print("выстрел:", total_rounds,
                  "боевой   ----",
                  "холостых:", holost,
                  "боевых:", boevie,
                  "осталось:", holost + boevie)

        else:
            print('заново введи')

        if total_rounds == rounds:
            time.sleep(0.5)
            print('\nrestart.....\n\n\n\n\n')
            time.sleep(0.5)
            buckshot_roulette()


        if (holost + boevie > 0) and (boevie >= 0) and ((type_shot in ('х', '[')) or (type_shot in ('б', ','))):
            print('шанс боевого:', round((boevie/(holost + boevie))*100),'%')


        
if __name__ == "__main__":
    buckshot_roulette()







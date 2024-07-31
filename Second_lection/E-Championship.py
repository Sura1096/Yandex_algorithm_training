'''
Ежегодный турнир «Веселый коровяк» — по метанию коровьих лепешек на дальность —
прошел 8–9 июля в селе Крылово Осинского района Пермского края.

К сожалению, после чемпионата потерялись записи с фамилиями участников,
остались только записи о длине броска в том порядке, в котором их совершали участники.

Трактиорист Василий помнит три факта:
1) Число метров, на которое он метнул лепешку, оканчивалось на 5
2) Один из победителей чемпионата метал лепешку до Василия
3) Участник, метавший лепешку сразу после Василия, метнул ее на меньшее количество метров

Будем считать, что участник соревнования занял k-е место,
если ровно (k − 1) участников чемпионата метнули лепешку строго дальше, чем он.

Какое максимально высокое место мог занять Василий?

Формат ввода
Первая строка входного файла содержит целое число n — количество участников чемпионата по метанию лепешек (3 ≤ n ≤ 105).
Вторая строка входного файла содержит n положительных целых чисел,
каждое из которых не превышает 1000, — дальность броска участников чемпионата, приведенные в том порядке,
в котором происходило метание.

Формат вывода
Выведите самое высокое место, которое мог занять тракторист Василий.
Если не существует ни одного участника чемпионата, который удовлетворяет, описанным выше условиям, выведите число 0.

ПРИМЕР 1
Ввод
7
10 20 15 10 30 5 1

Вывод
6

ПРИМЕР 2
Ввод
3
15 15 10

Вывод
1

ПРИМЕР 3
Ввод
3
10 15 20

Вывод
0
'''


def get_winner_pos(participants_amount: int, distances: list[int]) -> int:
    winner_pos = 0
    winner_metres = distances[0]
    for ind in range(1, participants_amount):
        if distances[ind] > winner_metres:
            winner_metres = distances[ind]
            winner_pos = ind
    return winner_pos


def get_vasyas_pos(participants_amount: int, winner_pos: int) -> tuple[int, int]:
    vasyas_pos = -1
    vasyas_distance = -1
    for ind in range(winner_pos + 1, participants_amount - 1):
        if distances[ind] % 10 == 5 and distances[ind + 1] < distances[ind] and vasyas_distance < distances[ind]:
            vasyas_pos = ind
            vasyas_distance = distances[ind]
    return vasyas_pos, vasyas_distance


def vasyas_place(participants_amount: int, distances: list[int]) -> int:
    winner_pos = get_winner_pos(participants_amount, distances)
    vasyas_pos, vasyas_distance = get_vasyas_pos(participants_amount, winner_pos)
    if vasyas_pos == -1:
        return 0

    place = 1
    for participant in distances:
        if participant > vasyas_distance:
            place += 1
    return place


participants_amount = int(input())
distances = list(map(int, input().split()))
print(vasyas_place(participants_amount, distances))

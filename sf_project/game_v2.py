"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    first_num = 1  # первое число в интервале выбора компьютера
    last_num = 101  # последнее число в интервале выбора компьютера
    while True:
        predict_number = np.random.randint(first_num, last_num)
        # предполагаемое число
        count += 1
        if number < predict_number:
            # если загаданное число меньше выбранного, область поиска
            # сокращается по верхнему пределу до выбраноого числа(не
            # включительно)
            last_num = predict_number
            continue
        if number > predict_number:
            # если загаданное число больше выбранного, область поиска
            # сокращается по нижнему пределу до выбраноого числа
            # (включительно)
            first_num = predict_number
            continue
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш
    алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

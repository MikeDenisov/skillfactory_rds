import numpy as np


def game_core_binary_search(number, max_value):
    count = 0
    predict = max_value
    while number != predict:
        count += 1
        step = (max_value // (2 ** count)) + 1

        if number > predict:
            predict += step
        elif number < predict:
            predict -= step
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    max_value = 100
    random_array = np.random.randint(1, max_value + 1, size=1000)
    for number in random_array:
        count_ls.append(game_core(number, max_value))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_binary_search)

import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
      count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    

def game_core_v3(number: int = 1) -> int:
    """ Угадываем число, сужая диапазон значений,
    с помощью записи наименьшего и наибольшего числа
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        Count (int): Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    smallest_number, biggest_number = 1, 100 #стандартные наибольшие и наименьшие значения
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        #сужаем диапазон в зависимости от predict
        if number > predict:
            smallest_number = predict + 1
        elif number < predict:
            biggest_number = predict - 1
        #Обновляем наш predict используя range от самого маленького числа, до большего
        predict = np.random.randint(smallest_number, biggest_number + 1)

    # Ваш код заканчивается здесь

    return count

    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
from functools import lru_cache

# Номінали монет
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result


@lru_cache(maxsize=None)  # Оптимізація за допомогою кешування
def find_min_coins(amount):
    if amount == 0:
        return {}

    min_coins = None
    best_combination = None

    for coin in COINS:
        if amount >= coin:
            remainder = amount - coin
            sub_result = find_min_coins(remainder) # Знаходимо оптимальне розбиття для залишку
            current_count = sum(sub_result.values()) + 1 # Підраховуємо кількість монет

            # Якщо це найменша кількість монет — зберігаємо це значення, як найкраще рішення
            if min_coins is None or current_count < min_coins: 
                min_coins = current_count 
                best_combination = sub_result.copy()
                best_combination[coin] = best_combination.get(coin, 0) + 1

    return best_combination
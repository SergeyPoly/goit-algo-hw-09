import time
from algorithms import find_coins_greedy, find_min_coins

def compare_algorithms(amount):
    start_time = time.perf_counter()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    dp_result = find_min_coins(amount)
    dp_time = time.perf_counter() - start_time

    print(f"\nСума: {amount}")
    print(f"Жадібний алгоритм: {greedy_result}, Час виконання: {greedy_time:.6f} сек.")
    print(f"Динамічне програмування: {dp_result}, Час виконання: {dp_time:.6f} сек.")


# --- Тестування ---
for amount in [113, 289, 567, 1000, 3582]:
    compare_algorithms(amount)
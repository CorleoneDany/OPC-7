import itertools
import time
from tqdm import tqdm

stocks = {
    "Action-1": [20, 5],
    "Action-2": [30, 10],
    "Action-3": [50, 15],
    "Action-4": [70, 20],
    "Action-5": [60, 17],
    "Action-6": [80, 25],
    "Action-7": [22, 7],
    "Action-8": [26, 11],
    "Action-9": [48, 13],
    "Action-10": [34, 27],
    "Action-11": [42, 17],
    "Action-12": [110, 9],
    "Action-13": [38, 23],
    "Action-14": [14, 1],
    "Action-15": [18, 3],
    "Action-16": [8, 8],
    "Action-17": [4, 12],
    "Action-18": [10, 14],
    "Action-19": [24, 21],
    "Action-20": [114, 18],
}


def return_keys(dict):
    """Returns a dict's keys."""
    return list(dict.keys())


def return_weight_list(dict):
    """Returns a list of weights from a dict."""
    keys_list = return_keys(dict)
    return [dict[key][0] for key in keys_list]


def return_profit_list(dict):
    """Returns a list of profits from a dict."""
    keys_list = return_keys(dict)
    return [dict[key][1] for key in keys_list]


def return_gains_list():
    """Returns a list of gains from a dict."""
    weight_list = return_weight_list()
    profit_list = return_profit_list()
    return [(int(weight_list[option]) * int(profit_list[option])) / 100
            for option in range(len(weight_list))]


def return_gain_from_key(dict, key):
    """Returns the gain from the dict's key."""
    stock_values = dict.get(key)
    weight = stock_values[0]
    profit = stock_values[1]
    return ((weight * profit) / 100)


def return_weight_from_key(dict, key):
    """Returns the weight from the dict's key."""
    stock_values = dict.get(key)
    return stock_values[0]


def return_profit_from_key(dict, key):
    """Returns the profit from the dict's key."""
    stock_values = dict.get(key)
    return stock_values[1]


def return_all_combinations(dict):
    """Returns all combinations from the dict."""
    result = []
    for L in range(len(dict) + 1):
        for subset in itertools.combinations(dict, L):
            result.append(subset)
    return result


def test_combination(combination, dict):
    """Returns the result of the given combination."""
    money = 500.0
    total_profit = 0.0
    for action in combination:
        if money >= return_weight_from_key(dict, action):
            total_profit += return_gain_from_key(dict, action)
            money -= return_weight_from_key(dict, action)
    return total_profit


def bruteforce(dict, combinations):
    """Returns the best options to buy from a dict and its combinations."""
    best_option = []
    best_gain = 0
    for option in tqdm(combinations):
        gain = test_combination(option, dict)
        if gain > best_gain:
            best_gain = gain
            best_option = option
    print(
        f"La meilleure option est la suivante : {best_option} et elle rapportera "
        f"{best_gain}€")


def brute_main():
    """Executes the bruteforce program."""
    print("Calcul en cours.")
    start = time.time()
    combinations = return_all_combinations(stocks)
    bruteforce(stocks, combinations)
    end = time.time()
    elapsed_time = round(end - start)
    print(
        f"L'éxécution du script bruteforce à prit environ {elapsed_time} secondes.\n"
    )


brute_main()

# Bruteforce = O(n ** 2)

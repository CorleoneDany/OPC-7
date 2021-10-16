import itertools


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


def return_keys():
	keys_list = stocks.keys()
	return keys_list


def return_weight_list():
	result = []
	keys_list = return_keys()
	for key in keys_list:
		result.append(stocks[key][0])
	return result


def return_profit_list():
	result = []
	keys_list = return_keys()
	for key in keys_list:
		result.append(stocks[key][1])
	return result


def return_gains_list():
	result = []
	weight_list = return_weight_list()
	profit_list = return_profit_list()
	for option in range(20):
		result.append(
			(int(weight_list[option]) * int(profit_list[option])) / 100)
	return result


def return_gain_from_key(key):
	stock_values = stocks.get(key)
	weight = stock_values[0]
	profit = stock_values[1]
	return ((weight * profit) / 100)


def return_weight_from_key(key):
	stock_values = stocks.get(key)
	return stock_values[0]


def return_profit_from_key(key):
	stock_values = stocks.get(key)
	return stock_values[1]


def return_all_combinations():
	result = []
	for L in range(0, len(stocks) + 1):
		for subset in itertools.combinations(stocks, L):
			result.append(subset)
	return result


def test_combination(combination):
	money = 500.0
	total_profit = 0.0
	for action in combination:
		if money >= return_weight_from_key(action):
			total_profit += return_gain_from_key(action)
			money -= return_weight_from_key(action)
	return total_profit


def bruteforce(combinations):
	best_option = []
	best_gain = 0
	for option in combinations:
		gain = test_combination(option)
		if gain > best_gain:
			best_gain = gain
			best_option = option
		else:
			print(f"{gain} est inférieur a {best_gain}")
	print(f"La meilleure option est la suivante : {best_option} et elle rapportera "
	f"{best_gain}")



combinations = return_all_combinations()
bruteforce(combinations)

# Bruteforce = O(n ** 2)

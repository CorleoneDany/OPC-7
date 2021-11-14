from optimised import *

import csv


def return_cleaned_dict(csv_file):
    """Returns the cleaned dict from a csv file."""
    cleaned_dict = {}
    with open(csv_file, mode="r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if float(row["profit"]) > 0 and float(row["price"]) > 0:
                cleaned_dict[row["name"]] = []
                cleaned_dict[row["name"]].append(
                    round(float(row["price"]) * 100))
                cleaned_dict[row["name"]].append(
                    round(float(row["price"]) * float(row["profit"])))
        return (cleaned_dict)


def optimised_tester(dict):
    """Returns the result from the knapsack algorithm from a dict."""
    start = time.time()
    print("Calcul en cours.")
    name_list = return_keys(dict)
    weights_list = return_weight_list(dict)
    gains_list = return_profit_list(dict)
    money = 500
    printknapSack(money * 100, weights_list, gains_list, name_list)
    end = time.time()
    elapsed_time = round(end - start)
    print(
        f"L'éxécution du script optimisé à prit environ {elapsed_time} secondes.\n"
    )


#return_cleaned_dict("dataset1.csv")
#return_cleaned_dict("dataset2.csv")
optimised_tester(return_cleaned_dict("dataset1.csv"))
optimised_tester(return_cleaned_dict("dataset2.csv"))

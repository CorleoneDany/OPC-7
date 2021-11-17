from bruteforce import *

# Python3 code for Dynamic Programming
# based solution for 0-1 Knapsack problem


# Prints the items which are put in a
# knapsack of capacity W
def printknapSack(W, wt, val, name_list):
    """Executes the knapsack algorithm from the list of values needed."""
    n = len(val)
    best_actions = []
    price_list = []
    total_price = 0
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # Build table K[][] in bottom
    # up manner
    for i in tqdm(range(n + 1)):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # stores the result of Knapsack
    res = K[n][W]
    print(f"Le meilleur revenu possible est de : {float(res) / 100}€")

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            best_actions.append(name_list[i - 1])
            price_list.append((wt[i - 1] / 100))

            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

    print(
        "Pour avoir les meilleurs revenus, sélectionner les options suivantes : "
    )
    for action_name, price in zip(best_actions, price_list):
        print(f"{action_name} au prix de {price}€")
        total_price += price

    print(f"Au final nous aurons dépensé {total_price}€ pour ce résultat.")


#Optimised = O(n)
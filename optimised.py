from bruteforce import *

# Python3 code for Dynamic Programming
# based solution for 0-1 Knapsack problem

# Prints the items which are put in a
# knapsack of capacity W
def printknapSack(W, wt, val, name_list):
    n = len(val)
    best_actions = []
    best_values = []
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
            
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                + K[i - 1][w - wt[i - 1]],
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
            best_values.append((wt[i - 1] / 100))

            
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
    
    #print(f"La meilleure suite d'action est la suivante : {best_actions}")
    print("Pour avoir les meilleurs revenus, sélectionner les options suivantes : ")
    #print(", ".join(str(action_name)) for action_name in best_actions)
    for action_name, best_value in zip(best_actions, best_values):
        print(f"{action_name} au prix de {best_value}€")
    #print(", ".join(str(float(action_value) / 100) for action_value in best_values))


#Optimised = O(n)

#Optimised ouvre un tableau n = capacity donc séparer capacity de money 
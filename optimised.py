from bruteforce import *

##################### SOLUTION 1 #####################

def solve_knapsack(profits, weights, capacity):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):

    # base case checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
        dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(
    dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]

##################### SOLUTION 2 #####################

def knapSack(W, wt, val): 
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif wt[i-1] <= j: 
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][W] 

##################### SOLUTION 3 #####################

# Prints the items which are put in a
# knapsack of capacity W
def printknapSack(W, wt, val, n):
    best_actions = []
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
            best_actions.append(wt[i - 1])
             
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
    
    print(f"Le meilleur revenu possible est de : {res}")
    print(f"La meilleure suite d'action est la suivante : {best_actions}")
    #print(", ".join(str(option) for option in best_actions))

def knapsack_main():
    gains_list = return_gains_list()
    weight_list = return_weight_list()
    length = len(gains_list)
    #print(solve_knapsack(gains_list, weight_list, 500))
    #print(knapSack(500, weight_list, gains_list))
    printknapSack(500, weight_list, gains_list, length)

knapsack_main()


#Optimised = O(n)

#Optimised ouvre un tableau n = capacity donc séparer capacity de money 
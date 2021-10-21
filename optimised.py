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

def knapsack_main():
    print(solve_knapsack(return_gains_list(), return_weight_list(), 500))
    print(knapSack(500, return_weight_list(), return_gains_list()))


#Optimised = O(n)
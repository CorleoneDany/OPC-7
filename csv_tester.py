from optimised import *

import csv 

def read_csv(csv_file):
    weight_list = []
    gain_list = []
    with open(csv_file) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            weight_list.append(float(row["price"]))
            gain_list.append((float(row["price"]) * float(row["profit"])) / 100)
        print(solve_knapsack(gain_list, weight_list, 500))

        #Le problème est que la capacité est parfois en float mais elle est utilisée 
        #en tant qu'index dans le tableau des 2 methodes knapsack

        #Multiplier toutes les valeurs par 100 puis les diviser ensuite par 100 ?

read_csv("dataset1.csv")
read_csv("dataset2.csv")
from optimised import *

import csv 

def read_csv(csv_file):
    weights_list = []
    gains_list = []
    money = 500
    with open(csv_file, mode="r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if float(row["profit"]) > 0 and float(row["price"]) > 0:
                weights_list.append(round(float(row["price"]) * 100))
                gains_list.append(round(float(row["price"]) * float(row["profit"])))
    printknapSack(money * 100, weights_list, gains_list)


        #Le problème est que la capacité est parfois en float mais elle est utilisée 
        #en tant qu'index dans le tableau des 2 methodes knapsack

        #Multiplier toutes les valeurs par 100 puis les diviser ensuite par 100 ?
        #Multiplier les valeurs par 100 ferait un algo bien plus lourd car le tableau
        #dynamique créé est plus gros lorsque la capacité est plus grosse donc dans ce cas
        #100 fois plus grosse

        #Arrondir l'argent restant au plus bas ? plus haut ? 
        #Ok si les résultats ne sont pas faussés a cause des centimes ce qui me semble
        #peu probable

        #Relire le fonctionnement de l'algo knapskack et le comprendre a 100%
        #index arrondi ou ifs ? corriger intelligement le soucis d'index

        #Se renseigner sur le discord P7, la solution y est peut être déjà
        #Corentin sur le P7

        #Separer la valeur argent et la valeur de taille de tableau
        #Ne pas oublier qu'une variable ne doit avoir qu'une seule utilité si possible 

read_csv("dataset1.csv")
read_csv("dataset2.csv")
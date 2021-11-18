from bruteforce import *
from csv_cleaner import *
from optimised import *

def main():
    brute_main()
    optimised_tester(return_cleaned_dict("dataset1.csv"))
    optimised_tester(return_cleaned_dict("dataset2.csv"))
from bruteforce import *
from csv_cleaner import *
from optimised import *

def main():
    brute_main()
    for file in open_files():
        optimised_tester(return_cleaned_dict(file))

main()
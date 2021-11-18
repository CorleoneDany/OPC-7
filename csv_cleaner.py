import csv
import tkinter as tk   # from tkinter import Tk for Python 3.x
from tkinter import filedialog

def open_files():
    """Opens a window to select the csv files needed."""
    gui = tk.Tk()
    gui.withdraw()
    return filedialog.askopenfilenames(initialdir=".",
                                          title="Veuillez choisir un fichier csv",
                                          filetypes= (("csv files","*.csv"),
                                          ("all files","*.*")))


def return_cleaned_dict(csv_file):
    """Returns the cleaned dict from a csv file."""
    cleaned_dict = {}
    with open(csv_file, mode="r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if float(row["profit"]) > 0 and float(row["price"]) > 0:
                cleaned_dict[row["name"]] = [
                    round(float(row["price"]) * 100),
                    round(float(row["price"]) * float(row["profit"])),
                ]

        return (cleaned_dict)


#return_cleaned_dict("dataset1.csv")
#return_cleaned_dict("dataset2.csv")


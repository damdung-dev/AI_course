import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from IPython.display import display

path_Data = "D:\\python_and_deeplearning_course\\lab\\connect_database\\"
checkPath = os.path.isdir(path_Data)
checkFile = os.path.isfile(path_Data + "grocery_dataset.txt")
print("The path and file are valid or not :", checkPath, checkFile)

grocery_items = set()
with open(path_Data + "grocery_dataset.txt") as f:
    reader = csv.reader(f, delimiter=",")
    for i, line in enumerate(reader):
        grocery_items.update(line)

display("-".join(grocery_items))
print(len(grocery_items))

output_list = list()
with open(path_Data + "grocery_dataset.txt") as f:
    reader = csv.reader(f, delimiter=",")
    for i, line in enumerate(reader):
        row_val = {item:0 for item in grocery_items}
        row_val.update({item:1 for item in line})
        output_list.append(row_val)

print(len(output_list), len(output_list[0]))
print(output_list[:5])

grocery_df = pd.DataFrame(output_list)
print(grocery_df)
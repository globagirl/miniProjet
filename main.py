import pandas as pd
import numpy as np
from functions.analyse import *
from functions.graphs import *
from functions.traitement import *


def charger_dataset(path):  # Charger un dataset
    print("chargement dataset ..")
    dataset = pd.read_excel(path)  # charger dataset file
    print("----------------------------------------------------------")
    return dataset


# Step 1:
df = charger_dataset('Datasets/Adidas_US_Sales.xlsx')

# Step 2:
affiche_details(df)
prod_max_(df, 'Operating Profit')
prod_min_(df, 'Operating Profit')
print("----------------------------------------------------------")

# Step 3:
print(correlation(df))

# Step 4:
affiche_missing(df)
print("Size before edits", df.shape)
df_mis = replace_missing_data(df, ['Price per Unit'])
df_rm = remove_missing_data(df)
print("Size After", df.shape)
df_dup = remove_dups(df_rm)
print("----------------------------------------------------------")

# Step 5:
df_clean = remove_unneeded_data(df_dup, ['Retailer ID', 'Region', 'State'])
dummy(df)  # création des dummy variables
discretisation()  # discrétisation des attributs
print("----------------------------------------------------------")

# Step 6:graphs
create_excel(df_clean, "clean_data")
print("----------------------------------------------------------")

import pandas as pd
import numpy as np
# import jupyterlab as jp
from functions.analyse import *
from functions.traitement import *


def import_excel(path):
    dataset = pd.read_excel(path)  # charger dataset file
    return dataset


df = import_excel('Datasets/Adidas_US_Sales.xlsx')
affiche_details(df)
prod_max_(df, 'Operating Profit')
prod_min_(df, 'Operating Profit')
# print("Before", df.shape)
# clean_data(df)
# print("After", df.shape)
print(df.describe())
# print(df.isnull().sum)



import pandas as pd
# import numpy as np


def affiche_details(dataset):
    print('Attributes list and their types: ', dataset.dtypes)  # liste et type des attributs
    print("Statistique: ", dataset.describe())  # valeurs minimales/maximales, moyenne, etc
    # Extra:
    print("Info: ", dataset.info())  # information about the data
    print("Attributes: ", dataset.columns)  # column headers
    print("Size(rows,columns): ", dataset.shape)


def prod_max_(df, column):
    print('Products that have maximum Operating Profit: ')
    print(df.loc[df[column] == df[column].max()])


def prod_min_(df, column):
    print('Products that have minimum Operating Profit: ')
    print(df.loc[df[column] == df[column].min()])  # display les lignes qui ont le min profit


def correlation(dataset):
    df = pd.DataFrame(dataset, columns=['Price per Unit', 'Operating Profit'])  # affiche specific column(s)
    print(df.corr())
    print("person corr")
    print(dataset[:10].corr())

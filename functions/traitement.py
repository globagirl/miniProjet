import pandas as pd
from sklearn import datasets


def affiche_missing(dataset):
    print("Missing data", dataset.isna())
    print("Sum of missing values:", dataset.isna().sum)  # afficher sum des valeurs manquantes


def remove_missing_data(dataset):
    print("Removing nulls:")
    dataset = dataset.dropna(axis=0)  # trait: Drop rows with element missing/axis=0 because we're removing lines
    return dataset


def remove_dups(dataset):
    print("Removing dupilcates:")
    dataset = dataset.drop_duplicates()  # trait: Remove duplicated info
    return dataset


def replace_missing_data(dataset, liste):
    dataset = dataset.fillna(dataset['Price per Unit'].mean())  # transformer) les valeurs manquantes
    return dataset


def remove_unneeded_data(dataset, liste):  # Supprimer les attributes inutiles
    # dataset.drop(liste, inplave=True, axis=1)
    print("Removing selected columns:")
    dataset = dataset.drop(columns=liste)
    return dataset


def dummy(dataset):
    dummy_tab = pd.get_dummies(dataset, prefix=None, prefix_sep='_', )
    print(dummy_tab)


def discretisation():
    digits = datasets.load_digits()
    print(digits)

    print(digits.images.shape)  # Dimensions
    print(digits.images)  # Sous forme d’un cube d’images 1797 x 8x8
    print(digits.data)  # Sous forme d’une matrice 1797 x 64
    print(digits.target)  # Label réel de chaque caractère

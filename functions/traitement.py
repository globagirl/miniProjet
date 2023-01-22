def clean_data(dataset):
    dataset.drop_duplicates()  # Remove duplicated info
    dataset.isna()  # affiche null val
    dataset.dropna()  #Drop the rows where at least one element is missing.


def remove_unneeded_data(dataset, liste):
    dataset.drop(liste, inplave=True, axis=1)

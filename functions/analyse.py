
def prod_max_(df, column):
    print('Products that have maximum Operating Profit: ')
    print(df.loc[df[column] == df[column].max()])


def prod_min_(df,column):
    print('Products that have minimum Operating Profit: ')
    print(df.loc[df[column] == df[column].min()])  # display les lignes qui ont le min profit


def affiche_details(dataset):
    print('Attributes list and their types: ')
    print(dataset.dtypes)  # liste et type des attributs
    print(dataset.info())  # information about the data
    print(dataset.columns.ravel())  # column headers
    print(dataset.shape)  # (columns,rows)

# data = pd.DataFrame(dataset, columns=['Units Sold'])  # specify column(s)

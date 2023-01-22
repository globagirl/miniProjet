import pandas as pd


def create_excel(df):
    # Create a Pandas Excel writer
    writer = pd.ExcelWriter('pandas_simple.xlsx')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.close()


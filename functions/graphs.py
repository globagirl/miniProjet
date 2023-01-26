import pandas as pd
import xlsxwriter as xlsxwriter
import matplotlib.pyplot as mp


def create_excel(df, filename):
    writer = pd.ExcelWriter('Datasets/'+filename+'.xlsx', engine='xlsxwriter')  # Create a Pandas Excel writer
    df.to_excel(writer, sheet_name='Sheet1')  # Convert the dataframe to an XlsxWriter Excel object.

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    chart = chart_1(workbook, df)

    worksheet.insert_chart('O2', chart)  # Insert the chart into the worksheet.
    writer.close()  # Close the Pandas Excel writer and output the Excel file.

    print("Find your results in "+filename+" excel file")


def chart_1(workbook, dataset):
    chart = workbook.add_chart({'type': 'column'})  # Create a chart object.


    # Configure the series of the chart from the dataframe data.
    chart.add_series({
        'values': '=Sheet1!$H:$H',
        'gap': 2,
    })

    # Configure the chart axes.Operating Profit
    chart.set_x_axis({'name': 'Products'})
    chart.set_y_axis({'name': 'Profit', 'major_gridlines': {'visible': False}})
    chart.set_legend({'position': 'none'})  # Turn off chart legend. It is on by default in Excel.

    # chart = dataset.plot.hist(x='Product', y=['Operating Profit', 'Total Sales'])

    return chart
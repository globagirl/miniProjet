import pandas as pd
# import xlsxwriter


def create_excel(df, filename):
    writer = pd.ExcelWriter('Datasets/'+filename+'.xlsx', engine='xlsxwriter')  # Create a Pandas Excel writer
    df.to_excel(writer, sheet_name='Sheet1')  # Convert the dataframe to an XlsxWriter Excel object.
    workbook = writer.book  # Get the xlsxwriter workbook and worksheet objects
    worksheet = writer.sheets['Sheet1']

    chart = chart_1(workbook, df)

    # # count profits sum per product all grouped by retailer name
    # grouped = df.groupby(['Retailer', 'Product'])['Operating Profit'].sum()
    # # convert to dataframe
    # df2 = grouped.to_frame().reset_index()
    worksheet.insert_chart('O2', chart)  # Insert the chart into the worksheet.
    writer.close()  # Close the Pandas Excel writer and output the Excel file.

    print("Find your results in "+filename+" excel file")


def chart_1(workbook, dataset):
    # Create a chart object
    chart = workbook.add_chart({'type': 'column'})

    # Configure the series of the chart from the dataframe data
    # adding data to chart
    chart.add_series({
        'name':       '=Sheet1!$I$1',
        'categories': '=Sheet1!$B$2:$B$100',
        'values':     '=Sheet1!$I$2:$I$100',
        'gap': 2
    })

    # set graph properties
    chart.set_title({'name': 'Retailer Profits'})
    chart.set_x_axis({'name': 'Retailer'})
    chart.set_y_axis({'name': 'Profit'})
    return chart

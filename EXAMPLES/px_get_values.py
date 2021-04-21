#!/usr/bin/env python
import openpyxl as px
import csv

def main():
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb.active  # <.>
    headers = next(ws.values)   # <.>
    with open('presdata.csv', 'w') as presdata_out:
        wtr = csv.writer(presdata_out)
        for row in ws.values:  # <.>
            print(row[:5])   # <.>
            wtr.writerow(row[:5])


if __name__ == '__main__':
    main()

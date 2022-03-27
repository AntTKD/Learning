# Created by: Ant_TKD
# Created in: IDLE 3.10
# Date: 27/03/2022

# File name: csv_split.py

# My goal is to read a spreadsheet, and copy select rows from that spreadsheet to a new spreadsheet depending on the value of one of the fields.

# I am still a beginner, and want to familiarise myslef with the standard librabry before I explore third party modules. 
import csv

# I'm using a spreadsheet of Yu-Gi-Oh! monster card details as I will be able to see more easily if the reading / copying goes wrong. 

csv_file = 'YGO_Mons.csv'

fields = ['Mon_Name','Mon_Lev_Ran_LRt','Mon_Type','Mon_Attribute','Mon_Atk','Mon_Def','Effect','Tuner','Mon_SubType']



with open(csv_file, 'r', newline = '\n', encoding = 'utf8') as file:
    # I'm saving the data I want to copy into a list.
    # Originally, I had wanted to write the row to the new spreadsheet whilst reading the original file.
    # But constantly closing and reopening the file meant that the first row of data was being continuously overwritten.
    # And only the last valid row was being copied to the new spreadsheet. 
    copy_data = []
    for Monster in csv.DictReader(file, fieldnames=fields, restkey=None, restval=None, dialect='excel', delimiter = ','):
        print(Monster)
        for column in fields:
            print(column,': ', Monster[column])
        if Monster['Mon_Attribute'] == 'LIGHT':
            copy_data.append(Monster) 
        print('\n')
file.close()
print('Extraction complete. \n')

# The final step of copying the data was made optional for testing purposes. 
comp_ex = input('Complete extraction?: ')

if comp_ex.lower() == 'yes':
    with open('Light_Mons.csv', 'w', newline = '\n') as csvL:
        writ_obj = csv.DictWriter(csvL, fieldnames = fields, restval='', extrasaction='raise', dialect='excel')
        writ_obj.writeheader()
        for Monster in copy_data:
            writ_obj.writerow(Monster)
    csvL.close()
else:
    print(copy_data)

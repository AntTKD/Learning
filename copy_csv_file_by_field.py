import csv

def get_fieldnames(csv_file):
    with open(csv_file, mode = 'r', encoding = 'utf-8-sig', newline = '\n') as file:
        fieldnames = (file.readline().strip()).split(',')
        return fieldnames

def get_values_from_field(csv_file, field):
    with open(csv_file, mode = 'r', encoding = 'utf-8-sig', newline = '\n') as file:
        field_values = []
        read_obj = csv.DictReader(file, fieldnames = get_fieldnames(csv_file), restkey = None, restval = None, dialect = 'excel')
        for row in read_obj:
            if (row[field] not in field_values) and row[field] != field:
                field_values.append(row[field])
        return sorted(list(field_values))       

def create_dict_from_list(list_object):
    key = 1
    output = {}
    for item in list_object:
        output[key] = item
        key += 1
    return output

def dict_options(list_object):
    dict_obj = create_dict_from_list(list_object)
    output = 0
    while output not in dict_obj:
        print('Please select one of the following fields: ')
        for key in dict_obj:
            print(f'\t{key} = {dict_obj[key]}')
        output = input('> ')
        try:
            if int(output) not in dict_obj:
                print('Please choose one of the numbered options above.\n')
                continue
            else:
                return dict_obj[int(output)]
        except:
            print('Please choose one of the numbered options above.\n')
            continue
        
def choose_field(csv_file):
    while True:
        csv_fields = get_fieldnames(csv_file)
        print('Displaying field names...')
        chosen_field = dict_options(csv_fields)
        print(f'You have chosen "{chosen_field}". This field contains the following values: ')
        for val in get_values_from_field(csv_file, chosen_field):
            print('\t', val)
        print('\nDo you wish to continue? \n\t Y = Yes, N = No')
        answer = 'undetermined'
        while answer not in ('Y','N','YES','NO'):
            answer = input('> ').upper()
            if answer not in ('Y','N','YES','NO'):
                print('Please choose a valid option.\n')
            continue
        if answer in ('N','NO'):
            print('\n')
            continue
        elif answer in ('Y','YES'):
            print(f'{chosen_field} selected.')
            return chosen_field

def create_new_table_names(csv_file, field):
    field_vals = get_values_from_field(csv_file, field)
    file_names = {}
    file_prefix = csv_file.removesuffix('.csv')
    for value in field_vals:
        file_names[value] = file_prefix + '_' + value + '.csv'
    return file_names

def split_csv_file_by_field(csv_file):
    # Returns a dictionary where the keys are the new file names and the values are lists of dictionary-spreadsheet-rows. 
    field_choice = choose_field(csv_file)
    table_name_dict = create_new_table_names(csv_file, field_choice)
    new_file_dictionaries = {}
    
    for value in table_name_dict.values():
        new_file_dictionaries[value] = []

    with open(csv_file, mode = 'r', encoding = 'utf-8-sig', newline = '\n') as file:
        field_values = []
        read_obj = csv.DictReader(file, fieldnames = get_fieldnames(csv_file), restkey = None, restval = None, dialect = 'excel')
        iterations = 0
        for row in read_obj:
            if iterations == 1:
                new_file_dictionaries[(table_name_dict[(row[field_choice])])].append(row)
            else: iterations += 1
    return new_file_dictionaries

def copy_csv_file_by_field(csv_file):
    new_file_data = split_csv_file_by_field(csv_file)

    for file_name in new_file_data.keys():
        with open(file_name, 'w', encoding = 'utf-8-sig', newline = '\n') as new_file:
            write_obj = csv.DictWriter(new_file, fieldnames = get_fieldnames(csv_file), dialect = 'excel')
            write_obj.writeheader()
            write_obj.writerows(new_file_data[file_name])
                
    print('\nData copy complete.')

copy_csv_file_by_field('YGO_Mons.csv')

import csv
import json
import pickle
import pprint

def create_dict(dict_name, company_list):
    with open('{}'.format(dict_name), 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=company_list[0].keys())
        writer.writeheader()
        writer.writerows(company_list)

def create_json(json_name, company_list):
    with open(f'{json_name}', 'w') as json_file:
        json_file.write(json.dumps(company_list))

def create_pickle(pickle_name, company_list):
    with open(f'{pickle_name}.pkl', 'wb') as f:
        pickle.dump(company_list, f)



def main():
    company_list = []
    with open(r"c:\Users\demirkiran hasan\OneDrive - The Boston Consulting Group, Inc\Documents\Excel files\Copy of Database error.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                line_count += 1
                # joined_row = [''.join(row)]
                # entry_list = joined_row[0].split(';')

                # print('HASAN0:  ', row)
                # print('HASAN1:  ', joined_row)
                # print('HASAN2:  ', entry_list )

                entry_dict = {}
                entry_dict['ID'] = row[0]
                entry_dict['Code'] = row[1]
                entry_dict['Name'] = row[3]
                entry_dict['Total FTEs'] = row[4]
                entry_dict['Total Revenue'] = row[5]
                entry_dict['Data Collection View'] = row[6]
                entry_dict['Region'] = row[7]
                entry_dict['Division'] = row[8]
                entry_dict['Industry Sector'] = row[9]
                entry_dict['Mapping Division'] = row[10]
                entry_dict['Note'] = row[11]
                entry_dict['Gamma'] = row[13]
                entry_dict['KT'] = row[14]

                company_list.append(entry_dict)
                # exit()

    # create_dict('my_dictionary', company_list)
    # create_json('my_json', company_list)
    create_pickle('my_pickle', company_list)

if __name__ == '__main__':
    main()


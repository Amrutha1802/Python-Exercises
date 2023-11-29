# ex-2 write a function that takes data.csv file path
# and returns a dictionary

import csv


def csv_to_dictionary(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader=csv.DictReader(file)
        output_dict=[row for row in csv_reader]
    return output_dict


file_path = 'data.csv' 
print(csv_to_dictionary(file_path))




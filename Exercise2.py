# ex-2 write a function that takes data.csv file path
# and returns a dictionary

import csv


def read_csv_to_dict(file_path):
    """
    Reads a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - data_list: A list of dictionaries where each dictionary represents a row in the CSV.
    """
    data_list = []
    try:
        with open(file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = list(csv_reader)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except e:
        print(f"An error occurred : {e}")
    return data_list


file_path = "data.csv"
print(read_csv_to_dict(file_path))
